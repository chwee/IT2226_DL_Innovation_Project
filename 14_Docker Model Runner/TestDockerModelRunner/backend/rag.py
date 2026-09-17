"""Minimal TF-IDF retrieval over the local knowledge base.

No embedding model or vector DB — just enough retrieval to make the RAG
mockup demonstrably work: chunk the knowledge-base files, score chunks
against a query with cosine similarity over TF-IDF weighted term vectors,
and return the top matches to use as LLM context.
"""

import math
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple

TOKEN_RE = re.compile(r"[a-zA-Z][a-zA-Z'\-]*")

# The knowledge-base .txt files use one of two hand-authored layouts:
#   1. "--- CHUNK 001 ---" ... "--- END CHUNK 001 ---" blocks with
#      [CHUNK ID] / [TOPIC] / [KEYWORDS] / [TRIGGERS] / CONTENT: metadata.
#   2. "SECTION N: TITLE" headers with free-form prose underneath.
# Both are parsed into the same Chunk shape below.
CHUNK_BLOCK_RE = re.compile(
    r"---\s*CHUNK\s+\S+\s*---(.*?)---\s*END CHUNK\s+\S+\s*---",
    re.DOTALL | re.IGNORECASE,
)
CHUNK_ID_RE = re.compile(r"\[CHUNK ID\]\s*(\S+)")
TOPIC_RE = re.compile(r"\[TOPIC\]\s*(.+)")
KEYWORDS_RE = re.compile(r"\[KEYWORDS\]\s*(.+)")
TRIGGERS_RE = re.compile(r"\[TRIGGERS\]\s*(.*?)(?=\n\s*\n|\nCONTENT:)", re.DOTALL)
CONTENT_RE = re.compile(r"CONTENT:\s*\n(.*?)(?=\n\[RELATED CHUNKS\]|\Z)", re.DOTALL)
SECTION_HEADER_RE = re.compile(r"^SECTION\s+\d+\s*:\s*(.+?)\s*$", re.MULTILINE)

MAX_CHUNK_CHARS = 1100


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in TOKEN_RE.findall(text)]


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


@dataclass
class Section:
    chunk_id: str
    topic: str
    search_text: str  # topic + keywords + triggers, for scoring only
    content: str       # the actual passage shown to the user / sent to the model


def _extract_chunk_style(text: str) -> List[Section]:
    sections = []
    for match in CHUNK_BLOCK_RE.finditer(text):
        block = match.group(1)
        chunk_id_m = CHUNK_ID_RE.search(block)
        topic_m = TOPIC_RE.search(block)
        keywords_m = KEYWORDS_RE.search(block)
        triggers_m = TRIGGERS_RE.search(block)
        content_m = CONTENT_RE.search(block)

        topic = topic_m.group(1).strip() if topic_m else "Untitled"
        content = content_m.group(1).strip() if content_m else block.strip()
        keywords = keywords_m.group(1).strip() if keywords_m else ""
        triggers = triggers_m.group(1).strip() if triggers_m else ""

        sections.append(
            Section(
                chunk_id=chunk_id_m.group(1).strip() if chunk_id_m else _slugify(topic),
                topic=topic,
                search_text=f"{topic}\n{topic}\n{keywords}\n{triggers}",
                content=content,
            )
        )
    return sections


def _extract_section_style(text: str) -> List[Section]:
    headers = list(SECTION_HEADER_RE.finditer(text))
    if not headers:
        return []
    sections = []
    for i, header in enumerate(headers):
        topic = header.group(1).strip()
        start = header.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[start:end]
        # Strip the "---" divider lines that bracket each section header.
        body = re.sub(r"^-{5,}\s*$", "", body, flags=re.MULTILINE).strip()
        sections.append(
            Section(
                chunk_id=_slugify(topic),
                topic=topic,
                search_text=f"{topic}\n{topic}",
                content=body,
            )
        )
    return sections


def _split_paragraphs(text: str, max_len: int = MAX_CHUNK_CHARS) -> List[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    pieces: List[str] = []
    current = ""
    for p in paragraphs:
        if current and len(current) + len(p) + 2 > max_len:
            pieces.append(current)
            current = p
        else:
            current = f"{current}\n\n{p}" if current else p
    if current:
        pieces.append(current)
    return pieces or ([text.strip()] if text.strip() else [])


@dataclass
class Chunk:
    source: str
    chunk_id: str
    topic: str
    text: str
    term_freq: Counter = field(default_factory=Counter)


class RagIndex:
    def __init__(self, data_dir: Path):
        self.data_dir = Path(data_dir)
        self.chunks: List[Chunk] = []
        self.doc_freq: Counter = Counter()
        self.reload()

    def reload(self) -> None:
        chunks: List[Chunk] = []
        for path in sorted(self.data_dir.glob("*")):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")

            sections = _extract_chunk_style(text) or _extract_section_style(text)
            if not sections:
                sections = [
                    Section(chunk_id=path.stem, topic=path.stem, search_text=path.stem, content=text)
                ]

            for section in sections:
                pieces = _split_paragraphs(section.content)
                multi = len(pieces) > 1
                for i, piece in enumerate(pieces):
                    chunk_id = f"{section.chunk_id}#{i + 1}" if multi else section.chunk_id
                    indexable = f"{section.search_text}\n{piece}"
                    chunks.append(
                        Chunk(
                            source=path.name,
                            chunk_id=chunk_id,
                            topic=section.topic,
                            text=piece,
                            term_freq=Counter(tokenize(indexable)),
                        )
                    )

        doc_freq: Counter = Counter()
        for chunk in chunks:
            doc_freq.update(chunk.term_freq.keys())

        self.chunks = chunks
        self.doc_freq = doc_freq

    def _idf(self, term: str) -> float:
        n = len(self.chunks) or 1
        df = self.doc_freq.get(term, 0)
        return math.log((n + 1) / (df + 1)) + 1.0

    def _vector(self, term_freq: Counter) -> dict:
        return {term: freq * self._idf(term) for term, freq in term_freq.items()}

    def search(self, query: str, top_k: int = 4) -> List[Tuple[float, Chunk]]:
        query_tokens = tokenize(query)
        if not query_tokens or not self.chunks:
            return []

        q_vec = self._vector(Counter(query_tokens))
        q_norm = math.sqrt(sum(v * v for v in q_vec.values())) or 1.0

        scored: List[Tuple[float, Chunk]] = []
        for chunk in self.chunks:
            c_vec = self._vector(chunk.term_freq)
            c_norm = math.sqrt(sum(v * v for v in c_vec.values())) or 1.0
            dot = sum(weight * c_vec.get(term, 0.0) for term, weight in q_vec.items())
            score = dot / (q_norm * c_norm)
            if score > 0:
                scored.append((score, chunk))

        scored.sort(key=lambda pair: pair[0], reverse=True)
        return scored[:top_k]
