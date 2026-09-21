L11 - AI VOICE AGENT LAB (STARTER PACK)
=======================================

Open the lab guide:  L11_Voice_Agent_Lab_Guide.docx

Work through it in order. Do the Setup section first, then Part A, then Part B.

WHAT IS IN HERE
---------------
  agent.py                 Part A skeleton  - 12 TODOs to fill in
  ingest_hr_policies.py    Part B skeleton  - 3 TODOs
  agentrag.py              Part B skeleton  - 6 TODOs
  hr_policies/             5 mock company policy documents (nothing to edit)
  requirements.txt         the Python packages to install
  .env.local.example       template for your API keys
                           (if your copy of this folder shows it as
                            env.local.example.txt instead, just rename it)
  .gitignore               keeps your keys and venv out of version control

The three .py files ALREADY RUN as Python (no syntax errors) - they just
do not do anything useful until you have filled in the TODOs.

QUICK COMMAND REFERENCE
-----------------------
  python -m venv .venv                      create the virtual environment
  .venv\Scripts\activate                    activate it (Windows)
  pip install -r requirements.txt           install the packages
  python agent.py download-files            pre-fetch the local models
  python agent.py console                   Part A - talk to your agent
  python ingest_hr_policies.py              Part B - build the vector database
  python agentrag.py console                Part B - talk to the HR agent
