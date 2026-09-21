"""
PART B, STEP 2 - HR POLICY VOICE AGENT WITH RAG

Extends the Part A pattern with a Retrieval-Augmented Generation tool.

The pipeline (STT / LLM / TTS / VAD / turn detection) is identical to
agent.py and has ALREADY BEEN FILLED IN for you further down - you proved
you can build it in Part A. The only new concept here is the
search_hr_policy tool: instead of answering from what the LLM already
"knows", the agent is instructed to call this tool first, which searches a
local ChromaDB vector database of mock HR policy documents and returns the
most relevant excerpts to answer from.

Before running this, build the vector database once:
    python ingest_hr_policies.py

Then:
    python agentrag.py console
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from pathlib import Path

import chromadb
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession, RunContext, function_tool
from livekit.plugins import groq, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv(".env.local")

DB_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "hr_policies"

# Opened once at import time and reused for every session/query - the
# collection is just a local on-disk index, so this is cheap to keep open.

# --- TODO B4 | Open the vector database once, at start-up ---------------
#     Guide step B4  |  Lecture: Slide 30 - warm-up and start-up
#     Write 2 lines here.


class HRAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(

            # --- TODO B5 | Write the grounding instructions -------------
            #     Guide step B5  |  Lecture: Slides 11, 41
            #     Write 10 lines here.

        )

    # --- TODO B6 | Declare the tool the LLM can call --------------------
    #     Guide step B6  |  Lecture: Slide 11 - Act
    #     Write 8 lines here.
    #     NOTE: Step B7 fills in the body of this method, indented one level further.

        # --- TODO B7 | Search the database and return the excerpts ------
        #     Guide step B7  |  Lecture: Slides 11, 31
        #     Write 12 lines here.
        #     NOTE: This code goes INSIDE the method you wrote in Step B6.


server = AgentServer()


# --- TODO B8 | Register the RAG agent under its own name ----------------
#     Guide step B8  |  Lecture: Slide 22 - session
#     Write 1 line here.

async def hr_agent(ctx: agents.JobContext):
    session = AgentSession(
        stt=groq.STT(model="whisper-large-v3-turbo", language="en"),
        llm=groq.LLM(model="openai/gpt-oss-120b"),
        tts=groq.TTS(model="canopylabs/orpheus-v1-english", voice="hannah"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    # --- TODO B9 | Start the session with the HR agent ------------------
    #     Guide step B9  |  Lecture: Slide 22
    #     Write 7 lines here.


if __name__ == "__main__":
    agents.cli.run_app(server)
