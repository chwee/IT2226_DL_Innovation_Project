# =============================================================================
# PART A - AI VOICE AGENT   (LiveKit + Groq)
#
# This is a SKELETON. All the plumbing has been written for you. The blanks
# are the parts taught in the L11 lecture: the five stack components, the
# agent's instructions, and how a call session is started.
#
# Open the lab guide at Part A and work through the steps in order. Each
# TODO below matches one numbered step, which gives you the exact code.
#
# When every TODO is done:
#     python agent.py console     talk through your own mic and speakers
#     python agent.py dev         test in the browser via LiveKit Console
# =============================================================================

import sys

# Windows' default console codepage (cp1252) can't render the emoji the CLI
# prints on startup; force UTF-8 so console/dev mode doesn't crash.
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from dotenv import load_dotenv

# --- TODO A1 | Import the framework and the plugins ---------------------
#     Guide step A1  |  Lecture: Slides 13, 14
#     Write 3 lines here.

# Deprecated in favor of livekit.agents.inference.TurnDetector, but kept here
# since that replacement runs via LiveKit's hosted inference API rather than
# fully locally, and this project is optimized to stay on free/local components.
from livekit.plugins.turn_detector.multilingual import MultilingualModel

# --- TODO A2 | Load your API keys ---------------------------------------
#     Guide step A2  |  Lecture: Lab setup
#     Write 1 line here.


# --- TODO A3 | Define the agent and its instructions --------------------
#     Guide step A3  |  Lecture: Slide 11 - Reason
#     Write 8 lines here.


# --- TODO A4 | Create the worker ----------------------------------------
#     Guide step A4  |  Lecture: Slide 12 - client-server
#     Write 1 line here.


# --- TODO A5 | Register the session entrypoint --------------------------
#     Guide step A5  |  Lecture: Slide 22 - call session
#     Write 1 line here.

async def my_agent(ctx: agents.JobContext):
    session = AgentSession(

        # --- TODO A6 | STT - Speech to Text -----------------------------
        #     Guide step A6  |  Lecture: Slides 4, 8, 27
        #     Write 1 line here.

        # --- TODO A7 | LLM - the reasoning engine -----------------------
        #     Guide step A7  |  Lecture: Slides 4, 11, 29
        #     Write 1 line here.

        # --- TODO A8 | TTS - Text to Speech -----------------------------
        #     Guide step A8  |  Lecture: Slides 4, 9, 33
        #     Write 1 line here.

        # --- TODO A9 | VAD - Voice Activity Detection -------------------
        #     Guide step A9  |  Lecture: Slides 17, 19
        #     Write 1 line here.

        # --- TODO A10 | Turn detection - end of utterance ---------------
        #     Guide step A10  |  Lecture: Slides 17, 21, 26
        #     Write 1 line here.

    )

    # --- TODO A11 | Start the session and speak first -------------------
    #     Guide step A11  |  Lecture: Slides 18, 22
    #     Write 4 lines here.


# --- TODO A12 | Run the command-line app --------------------------------
#     Guide step A12  |  Lecture: Lab setup
#     Write 2 lines here.
