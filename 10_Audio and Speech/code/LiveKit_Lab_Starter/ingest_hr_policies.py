# =============================================================================
# PART B, STEP 1 - BUILD THE KNOWLEDGE BASE
#
# Reads every policy document in hr_policies/, splits each one into
# section-sized chunks, and stores them in a local ChromaDB vector database
# that the voice agent will search at question time.
#
# Run it once before starting agentrag.py, and again whenever you edit a
# policy file:
#     python ingest_hr_policies.py
# =============================================================================

import re
from pathlib import Path

import chromadb

POLICY_DIR = Path(__file__).parent / "hr_policies"
DB_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "hr_policies"


def chunk_markdown(text: str, source: str) -> list[dict]:
    """Split a markdown doc into one chunk per '## ' section."""

    # --- TODO B1 | Split each document into section chunks --------------
    #     Guide step B1  |  Lecture: Slide 31 - context and chunking
    #     Write 10 lines here.


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_DIR))

    # Drop and recreate so re-running this script always reflects the
    # current contents of hr_policies/*.md, with no stale/duplicate chunks.
    existing_names = {c.name for c in client.list_collections()}
    if COLLECTION_NAME in existing_names:
        client.delete_collection(COLLECTION_NAME)
    collection = client.create_collection(COLLECTION_NAME)

    # --- TODO B2 | Collect the chunks, their metadata and their ids -----
    #     Guide step B2  |  Lecture: Slide 31 - semantic caching
    #     Write 8 lines here.

    # Chroma's default embedding function (a small local ONNX MiniLM model,
    # downloaded once on first use) turns each chunk of text into a vector so
    # semantically similar questions and policy text can be matched later.

    # --- TODO B3 | Store the chunks in the vector database --------------
    #     Guide step B3  |  Lecture: Slide 31 - vector database
    #     Write 1 line here.

    print(
        f"Ingested {len(documents)} chunks from {len(policy_files)} policy files "
        f"into '{COLLECTION_NAME}' at {DB_DIR}"
    )


if __name__ == "__main__":
    main()
