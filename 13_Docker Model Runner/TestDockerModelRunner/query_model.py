#!/usr/bin/env python3
"""Standalone console client for Docker Model Runner's OpenAI-compatible API.

No third-party dependencies (stdlib only) — run with any Python 3.8+.

Usage:
    python query_model.py "What is CHAS?"
    python query_model.py "What is CHAS?" --model docker.io/ai/ministral3:8B-Q4_K_M
    python query_model.py "What is CHAS?" --no-stream
    python query_model.py                       # interactive mode, one question per line

Run `docker model list` to see which models are pulled and available to query.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

DEFAULT_BASE_URL = "http://localhost:12434/engines/v1"
DEFAULT_MODEL = "docker.io/ai/ministral3:8B-Q4_K_M"


def ask(base_url: str, model: str, question: str, stream: bool, max_tokens: int) -> None:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": question}],
        "max_tokens": max_tokens,
        "temperature": 0.2,
        "stream": stream,
    }
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=900) as resp:
            if stream:
                _print_stream(resp)
            else:
                _print_full(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"HTTP {e.code} error from Docker Model Runner: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(
            f"Could not reach Docker Model Runner at {base_url}: {e.reason}\n"
            "Is Docker Desktop running with Model Runner enabled?",
            file=sys.stderr,
        )
        sys.exit(1)


def _print_full(resp) -> None:
    data = json.loads(resp.read())
    try:
        message = data["choices"][0]["message"]
    except (KeyError, IndexError):
        print(f"Unexpected response: {data}", file=sys.stderr)
        sys.exit(1)
    if message.get("reasoning_content"):
        print(f"[reasoning]\n{message['reasoning_content']}\n")
    print(message.get("content", ""))


def _print_stream(resp) -> None:
    for raw_line in resp:
        line = raw_line.decode("utf-8", errors="replace").strip()
        if not line.startswith("data:"):
            continue
        data_str = line[len("data:"):].strip()
        if data_str == "[DONE]":
            break
        try:
            obj = json.loads(data_str)
        except json.JSONDecodeError:
            continue
        delta = (obj.get("choices") or [{}])[0].get("delta", {})
        if delta.get("reasoning_content"):
            print(delta["reasoning_content"], end="", flush=True)
        if delta.get("content"):
            print(delta["content"], end="", flush=True)
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("question", nargs="?", help="Question to ask. Omit for interactive mode.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"Default: {DEFAULT_BASE_URL}")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Default: {DEFAULT_MODEL}")
    parser.add_argument("--max-tokens", type=int, default=500)
    parser.add_argument("--no-stream", action="store_true", help="Wait for the full response instead of streaming tokens.")
    args = parser.parse_args()

    stream = not args.no_stream

    if args.question:
        ask(args.base_url, args.model, args.question, stream, args.max_tokens)
        return

    print(f"Model: {args.model}  |  {args.base_url}  (Ctrl+C to quit)")
    try:
        while True:
            question = input("\n> ").strip()
            if not question:
                continue
            ask(args.base_url, args.model, question, stream, args.max_tokens)
    except (KeyboardInterrupt, EOFError):
        print()


if __name__ == "__main__":
    main()
