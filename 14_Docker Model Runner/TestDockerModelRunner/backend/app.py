import json
import os
import time
from pathlib import Path
from typing import AsyncIterator, List, Optional, Tuple

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from rag import Chunk, RagIndex

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = Path(os.environ.get("DATA_DIR", "data/sample"))
if not DATA_DIR.is_absolute():
    DATA_DIR = (BASE_DIR / DATA_DIR).resolve()

DMR_BASE_URL = os.environ.get("DMR_BASE_URL", "http://localhost:12434/engines/v1").rstrip("/")
DMR_MODEL = os.environ.get("DMR_MODEL", "ai/gpt-oss:latest")
RAG_TOP_K = int(os.environ.get("RAG_TOP_K", "4"))
MAX_TOKENS = int(os.environ.get("RAG_MAX_TOKENS", "800"))
# gpt-oss is a reasoning model — "low" keeps its chain-of-thought short so
# answers (streamed or not) arrive faster. Set to "medium"/"high" for deeper
# reasoning at the cost of latency.
REASONING_EFFORT = os.environ.get("REASONING_EFFORT", "low")

# Large models can take minutes to load into memory on first use (cold start),
# so the read timeout for chat needs to be generous even though connect should be fast.
CHAT_TIMEOUT = httpx.Timeout(connect=10, read=900, write=30, pool=10)

SYSTEM_PROMPT = (
    "You are the OralLink assistant. Answer the user's question using only the "
    "information in the provided context. Cite the passages you used with their "
    "[n] marker. If the context does not contain the answer, say you don't know "
    "and suggest contacting OralLink directly rather than guessing."
)

app = FastAPI(title="OralLink RAG Tester")

rag_index = RagIndex(DATA_DIR)

# The model actually used for chat completions. Starts from DMR_MODEL but can
# be switched at runtime via POST /api/model to any model already pulled into
# Docker Model Runner (see GET /api/models), without restarting the app.
current_model = DMR_MODEL


class AskRequest(BaseModel):
    question: str
    top_k: Optional[int] = None


class SelectModelRequest(BaseModel):
    model: str


class SourceOut(BaseModel):
    n: int
    source: str
    topic: str
    chunk_id: str
    score: float
    text: str


class AskResponse(BaseModel):
    answer: str
    model: str
    sources: List[SourceOut]


ResultList = List[Tuple[float, Chunk]]


def _retrieve(question: str, top_k: int) -> Tuple[ResultList, str]:
    results = rag_index.search(question, top_k=top_k)
    if not results:
        context_block = "No relevant passages were found in the knowledge base."
    else:
        context_block = "\n\n".join(
            f"[{i + 1}] ({chunk.source} — {chunk.topic})\n{chunk.text}"
            for i, (_, chunk) in enumerate(results)
        )
    return results, context_block


def _sources_out(results: ResultList) -> List["SourceOut"]:
    return [
        SourceOut(
            n=i + 1,
            source=chunk.source,
            topic=chunk.topic,
            chunk_id=chunk.chunk_id,
            score=round(score, 4),
            text=chunk.text,
        )
        for i, (score, chunk) in enumerate(results)
    ]


def _chat_payload(context_block: str, question: str, stream: bool) -> dict:
    return {
        "model": current_model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Context:\n{context_block}\n\nQuestion: {question}"},
        ],
        "temperature": 0.2,
        "max_tokens": MAX_TOKENS,
        "reasoning_effort": REASONING_EFFORT,
        "stream": stream,
    }


@app.get("/api/config")
async def get_config():
    return {
        "base_url": DMR_BASE_URL,
        "model": current_model,
        "data_dir": str(DATA_DIR),
        "chunks_indexed": len(rag_index.chunks),
        "top_k": RAG_TOP_K,
    }


@app.post("/api/model")
async def select_model(req: SelectModelRequest):
    """Switch which model chat requests use, without restarting the app.

    Only models Docker Model Runner already has pulled are accepted — this
    app never triggers a pull itself, so `docker model pull` must be run
    beforehand for any model that should show up here.
    """
    global current_model
    model = req.model.strip()
    if not model:
        raise HTTPException(status_code=400, detail="model must not be empty")

    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.get(f"{DMR_BASE_URL}/models")
            resp.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Could not reach Docker Model Runner at {DMR_BASE_URL}: {e}",
            )
    available = {m.get("id") for m in resp.json().get("data", [])}
    if model not in available:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Model '{model}' is not pulled into Docker Model Runner. "
                f"Run `docker model pull {model}` first, or pick one of: "
                f"{', '.join(sorted(available)) or '(none pulled)'}"
            ),
        )

    current_model = model
    return {"model": current_model}


@app.get("/api/sources")
async def list_sources():
    counts: dict = {}
    for chunk in rag_index.chunks:
        counts[chunk.source] = counts.get(chunk.source, 0) + 1
    return {"sources": [{"file": f, "chunks": c} for f, c in sorted(counts.items())]}


@app.post("/api/reload")
async def reload_index():
    rag_index.reload()
    return {"chunks_indexed": len(rag_index.chunks)}


@app.get("/api/models")
async def list_models():
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            resp = await client.get(f"{DMR_BASE_URL}/models")
            resp.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Could not reach Docker Model Runner at {DMR_BASE_URL}: {e}",
            )
    return resp.json()


@app.post("/api/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    question = req.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="question must not be empty")

    top_k = req.top_k or RAG_TOP_K
    results, context_block = _retrieve(question, top_k)
    payload = _chat_payload(context_block, question, stream=False)

    async with httpx.AsyncClient(timeout=CHAT_TIMEOUT) as client:
        try:
            resp = await client.post(f"{DMR_BASE_URL}/chat/completions", json=payload)
            resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
        except httpx.TimeoutException as e:
            raise HTTPException(
                status_code=504,
                detail=(
                    f"Docker Model Runner did not respond in time for model "
                    f"'{current_model}'. Large models can take several minutes to load "
                    f"into memory on first use — try again, it should be faster once "
                    f"loaded. ({e})"
                ),
            )
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Could not reach Docker Model Runner at {DMR_BASE_URL}: {e}",
            )

    data = resp.json()
    try:
        answer = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        raise HTTPException(status_code=502, detail=f"Unexpected response from Docker Model Runner: {data}")

    return AskResponse(answer=answer, model=current_model, sources=_sources_out(results))


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


async def _stream_events(question: str, top_k: int) -> AsyncIterator[str]:
    started = time.perf_counter()
    results, context_block = _retrieve(question, top_k)
    yield _sse("sources", {"sources": [s.model_dump() for s in _sources_out(results)]})

    payload = _chat_payload(context_block, question, stream=True)

    try:
        async with httpx.AsyncClient(timeout=CHAT_TIMEOUT) as client:
            async with client.stream("POST", f"{DMR_BASE_URL}/chat/completions", json=payload) as resp:
                if resp.status_code >= 400:
                    body = await resp.aread()
                    yield _sse("error", {"detail": body.decode(errors="replace")})
                    return
                async for line in resp.aiter_lines():
                    if not line.startswith("data:"):
                        continue
                    raw = line[len("data:"):].strip()
                    if raw == "[DONE]":
                        break
                    try:
                        obj = json.loads(raw)
                    except json.JSONDecodeError:
                        continue
                    delta = (obj.get("choices") or [{}])[0].get("delta", {})
                    if delta.get("reasoning_content"):
                        yield _sse("reasoning", {"delta": delta["reasoning_content"]})
                    if delta.get("content"):
                        yield _sse("token", {"delta": delta["content"]})
    except httpx.TimeoutException as e:
        detail = (
            f"Docker Model Runner did not respond in time for model "
            f"'{current_model}'. Large models can take several minutes to load "
            f"into memory on first use — try again, it should be faster once "
            f"loaded. ({e})"
        )
        yield _sse("error", {"detail": detail})
        return
    except httpx.HTTPError as e:
        yield _sse("error", {"detail": f"Could not reach Docker Model Runner at {DMR_BASE_URL}: {e}"})
        return

    yield _sse("done", {"model": current_model, "elapsed": round(time.perf_counter() - started, 2)})


@app.post("/api/ask/stream")
async def ask_stream(req: AskRequest):
    question = req.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="question must not be empty")

    top_k = req.top_k or RAG_TOP_K
    return StreamingResponse(
        _stream_events(question, top_k),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


app.mount("/", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")
