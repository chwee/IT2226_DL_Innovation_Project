# AI Innovation with Deep Learning

**17-Week Industry-Focused Curriculum · 68 Contact Hours · 4 Hours / Week**

A production-oriented deep learning curriculum that takes learners from problem framing
through model engineering, generative and agentic AI, multimodal systems, guardrails,
full-stack application development, containerised deployment, and career readiness.

The course is deliberately *practitioner-first*: every week produces an artefact
(a spec, a benchmark, a pipeline, a container, a safety card, a pitch) rather than a
notebook that ends at `model.fit()`.

---

## Table of Contents

- [Learning Outcomes](#learning-outcomes)
- [Curriculum Overview](#curriculum-overview)
- [Weekly Breakdown](#weekly-breakdown)
  - [Phase 1 — Foundations, Problem Framing & AI-Assisted Development](#phase-1--foundations-problem-framing--ai-assisted-development)
  - [Phase 2 — Model Engineering & Optimisation](#phase-2--model-engineering--optimisation)
  - [Phase 3 — GenAI & Agentic Systems](#phase-3--genai--agentic-systems)
  - [Phase 4 — Multimodal AI Systems](#phase-4--multimodal-ai-systems)
  - [Phase 5 — Trust, Safety & Guardrails](#phase-5--trust-safety--guardrails)
  - [Phase 6 — Application Development](#phase-6--application-development)
  - [Phase 7 — Containerised & Agentic Deployment](#phase-7--containerised--agentic-deployment)
  - [Phase 8 — Career Readiness](#phase-8--career-readiness)
- [Learning Outcome Coverage Matrix](#learning-outcome-coverage-matrix)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Licence](#licence)

---

## Learning Outcomes

| # | Outcome |
|---|---------|
| **LO1** | Identify deep learning solutions for real-world problems by highlighting technical and practical issues. |
| **LO2** | Construct deep learning solutions using industry best practices and responsible AI principles. |
| **LO3** | Deploy deep learning solutions using industry-standard platforms. |
| **LO4** | Perform effectively in technical interviews and project a positive, consistent professional image to prospective employers. |

---

## Curriculum Overview

| Phase | Weeks | Track |
|-------|-------|-------|
| Phase 1 | 1–3 | Foundations, Problem Framing & AI-Assisted Development |
| Phase 2 | 4–5 | Model Engineering & Optimisation |
| Phase 3 | 6–8 | GenAI & Agentic Systems |
| Phase 4 | 9–10 | Multimodal AI Systems |
| Phase 5 | 11 | Trust, Safety & Guardrails |
| Phase 6 | 12–13 | Application Development |
| Phase 7 | 14–15 | Containerised & Agentic Deployment |
| Phase 8 | 16–17 | Career Readiness |

---

## Weekly Breakdown

### Phase 1 — Foundations, Problem Framing & AI-Assisted Development

<details open>
<summary><strong>Week 1 · Design Thinking for AI Product Development</strong> (4 hrs) — <em>LO1, LO2</em></summary>

**Topics**

- Design Thinking framework: Empathise → Define → Ideate → Prototype → Test
- Mapping real-world problems to AI/ML solution types
- Problem scoping canvas: stakeholders, success metrics, data feasibility
- AI opportunity assessment: where deep learning adds value vs simpler methods
- Build-vs-buy-vs-fine-tune decision framework for industry AI projects
- Case studies: Google Flood Forecasting, Microsoft Seeing AI, Waymo

**Learning Objectives**

- Apply the five Design Thinking stages to scope an AI product problem
- Produce a one-page Problem Framing Canvas for a chosen domain
- Distinguish problems that warrant deep learning from simpler ML approaches
- Apply the build-vs-buy-vs-fine-tune framework to a given business scenario
- Identify key stakeholders and define measurable success criteria

**Summary**

This session repositions learners from *student building models* to *practitioner solving
problems*. Using Stanford d.school's Design Thinking methodology, learners run a condensed
empathy-interview simulation and complete a Problem Framing Canvas. Three real industry case
studies (healthcare, mobility, accessibility) are deconstructed to show how problem framing
shapes architecture and tooling decisions later in the course. A structured
build-vs-buy-vs-fine-tune decision tree is introduced — a core industry skill for scoping AI
projects against real budget and time constraints. Learners leave with a shortlisted project
problem statement that carries through to their capstone.

</details>

<details>
<summary><strong>Week 2 · Vibe Programming: Spec-Driven Development with Claude Code</strong> (4 hrs) — <em>LO1, LO2</em></summary>

**Topics**

- What is "vibe coding"? Prompt-driven development and its limits at production scale (Andrej Karpathy)
- From vibe coding to spec-driven development: writing specs and acceptance criteria before prompting
- Spec-driven workflows: Claude Code's plan mode, GitHub Spec Kit, and spec-first agent patterns
- Claude Code: agentic CLI coding, project-level context, and multi-file edits
- Writing an effective technical spec: user stories, data model, API contract, edge cases
- Prompt engineering for code generation: context, constraints, and worked examples
- Reviewing AI-generated code: correctness, security, hallucinated APIs, and dependency risk
- Comparing Claude Code, GitHub Copilot, and Cursor: workflows and when each excels

**Learning Objectives**

- Distinguish vibe coding from spec-driven development and explain when each is appropriate
- Draft a one-page technical spec (user stories, data model, acceptance criteria) for a chosen feature
- Use Claude Code to implement a feature end-to-end from a written spec, from the terminal
- Critically evaluate AI-generated code for correctness, security, and alignment with the spec
- Compare Claude Code, GitHub Copilot, and Cursor and select the right tool for a given scenario

**Summary**

Loosely prompted "vibe coding" is fast to start but breaks down once a project grows past a few
files — the model loses track of intent and learners lose the ability to defend their own code.
This session introduces spec-driven development as the production-grade evolution of vibe coding:
learners write a short, structured spec for a feature of their own project *before* writing a
single prompt. Using Claude Code's agentic CLI and plan mode, learners then implement the feature
against that spec, experiencing how a written spec keeps a multi-file agentic edit anchored and
reviewable. The session closes with a critical code-review exercise, reinforcing that the human
remains the architect and reviewer of record.

</details>

<details>
<summary><strong>Week 3 · AI Ethics and Governance Overview</strong> (4 hrs) — <em>LO1, LO2</em></summary>

**Topics**

- Foundations of AI ethics: fairness, accountability, transparency, privacy
- Bias in AI systems: sources, types, and real-world impact
- AI governance frameworks: Singapore Model AI Governance Framework and IMDA/AI Verify
- Responsible AI principles: Singapore Body of Knowledge (BoK)
- AI and the law: GDPR/PDPA, intellectual property, liability, and emerging legislation
- Case studies: COMPAS recidivism, facial recognition policing, AI in hiring
- Organisational AI governance: policy templates, roles, and accountability structures

**Learning Objectives**

- Identify and explain the core principles of responsible AI (fairness, accountability, transparency)
- Map a given AI use-case to a governance risk tier and describe compliance obligations
- Distinguish between bias in data, algorithms, explainability, and deployment contexts
- Evaluate a case study of AI harm and propose mitigation strategies
- Draft a one-page AI governance policy for a hypothetical organisation

**Summary**

This foundational session establishes the ethical and regulatory literacy every AI practitioner
needs before building production systems. Learners survey the governance landscape — Singapore's
Model AI Governance Framework and BoK, alongside GDPR/PDPA — and understand how these frameworks
translate into technical and organisational obligations. Real-world case studies ground the
discussion in documented harms. The session shifts mindset: responsible AI is not a compliance
checkbox but a core engineering discipline shaping every technical decision for the rest of the
course.

</details>

### Phase 2 — Model Engineering & Optimisation

<details>
<summary><strong>Week 4 · Model Optimisation with ONNX</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- From notebook to production: the model-serving performance gap
- ONNX (Open Neural Network Exchange): a framework-agnostic model format
- Exporting PyTorch/TensorFlow models to ONNX: tracing vs scripting, dynamic axes
- Graph optimisation in ONNX Runtime: operator fusion, constant folding
- Quantisation strategies: post-training INT8/FP16 vs quantisation-aware training
- Serving with ONNX Runtime: CPU/GPU execution providers and batching
- Benchmarking: latency, throughput, memory footprint, and accuracy delta
- Where ONNX fits vs TensorRT, OpenVINO, and native framework serving

**Learning Objectives**

- Export a trained deep learning model to ONNX and verify numerical parity with the source model
- Apply post-training INT8 quantisation and benchmark the latency-vs-accuracy trade-off
- Serve an ONNX model using ONNX Runtime with an appropriate execution provider
- Benchmark and report latency, throughput, and memory footprint before and after optimisation
- Justify an optimisation strategy for a given deployment constraint (edge, mobile, or cloud)

**Summary**

A model that performs well in a notebook is not automatically ready for production. This session
focuses entirely on ONNX as the industry-standard bridge between training frameworks and
deployment targets. Learners export a trained model to ONNX, verify numerically consistent
outputs, and apply INT8 post-training quantisation using ONNX Runtime. A structured benchmarking
exercise compares original and optimised models on latency, throughput, and memory footprint. The
session closes by positioning ONNX within the wider optimisation landscape (TensorRT, OpenVINO).

</details>

<details>
<summary><strong>Week 5 · Fine-Tuning, LoRA & HuggingFace Production Pipelines</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- HuggingFace production ecosystem: `transformers`, `datasets`, `evaluate`, `accelerate`, `peft`
- Parameter-efficient fine-tuning (PEFT): LoRA, QLoRA, and adapter layers
- HuggingFace Trainer API and Accelerate for multi-GPU and mixed-precision training
- Experiment tracking integration: Weights & Biases with HuggingFace Trainer
- Model packaging and versioning: HuggingFace Hub and MLflow Model Registry
- Industry deployment patterns: batch inference, streaming APIs, serverless endpoints
- Production use-cases: contract analysis, support-ticket triage, clinical-notes classification

**Learning Objectives**

- Fine-tune a transformer model using LoRA via the PEFT library with W&B experiment tracking
- Compare full fine-tuning vs LoRA vs QLoRA on GPU memory, training time, and F1 score
- Package and register a fine-tuned model to HuggingFace Hub or MLflow Model Registry
- Design a production NLP inference architecture for a specified industry task at scale
- Select and justify a fine-tuning strategy for a given business constraint

**Summary**

Assuming prior knowledge of Transformer architecture, this session focuses entirely on production
fine-tuning engineering. Learners implement LoRA fine-tuning with PEFT and full experiment
tracking via Weights & Biases, using the `banking77` intent-classification dataset on a free Colab
T4 GPU. A structured benchmark compares full fine-tuning, LoRA, and QLoRA on GPU memory and
accuracy. The session emphasises versioning discipline: every experiment tracked, every model
registered and reproducible.

</details>

### Phase 3 — GenAI & Agentic Systems

<details>
<summary><strong>Week 6 · Retrieval-Augmented Generation (RAG) Systems</strong> (4 hrs) — <em>LO1, LO2, LO3</em></summary>

**Topics**

- RAG architecture: retriever + generator pipeline
- Vector databases: FAISS, Chroma, Pinecone — selecting the right store for production
- Embedding models: sentence-transformers, OpenAI embeddings, domain adaptation
- LangChain and LlamaIndex orchestration frameworks
- Evaluation: the RAGAs framework — faithfulness, answer relevancy, context precision/recall
- Industry use-cases: enterprise Q&A, document search, customer-support bots
- Production RAG patterns: chunking strategies, hybrid search, re-ranking

**Learning Objectives**

- Build an end-to-end RAG pipeline over a PDF corpus using LangChain and Chroma
- Select and justify an embedding model for a given domain
- Evaluate RAG output quality using RAGAs metrics
- Identify failure modes: hallucination, out-of-context retrieval, chunking errors
- Design a production RAG architecture with hybrid search and re-ranking

**Summary**

RAG is the dominant production pattern for enterprise LLM applications. Learners build a document
Q&A system over technical PDFs, comparing two chunking strategies and two embedding models, then
evaluating quality with RAGAs and metric-thresholding across Faithfulness, Answer Relevancy,
Context Precision, and Context Recall. Advanced production topics — hybrid dense/sparse retrieval
and cross-encoder re-ranking — show the gap between a demo and a production system. The
responsible AI component addresses hallucination risk in high-stakes domains.

</details>

<details>
<summary><strong>Week 7 · Agentic AI — Single-Agent Systems</strong> (4 hrs) — <em>LO1, LO2, LO3</em></summary>

**Topics**

- Agent anatomy: LLM + tools + memory + control loop
- The ReAct pattern: interleaving reasoning and tool calls
- Function/tool calling with OpenAI-compatible and Anthropic APIs
- Structured output and schema-constrained generation (Pydantic, JSON schema)
- Building a single-agent graph with LangGraph: nodes, edges, and state
- Tool integration: web search, code execution, and database/API queries
- Memory patterns: short-term context-window memory vs long-term vector-store memory
- Failure modes of single agents: looping, tool misuse, hallucinated tool calls

**Learning Objectives**

- Build a ReAct-style single agent that uses at least two tools to complete a task
- Implement function/tool calling against a live API
- Constrain agent output to a defined schema and validate it programmatically
- Diagnose and fix common single-agent failure modes
- Design a single-agent architecture diagram for a specified business task

**Summary**

This session establishes the building blocks of agentic AI before scaling to multi-agent systems.
Learners build a single ReAct-style agent with LangGraph that can search the web, run Python code,
and query a mock database — with state and control flow made explicit as a graph. Structured
output is enforced with Pydantic/JSON schema so downstream systems can consume results reliably.
A debugging lab exposes infinite tool loops, wrong tool selection, and hallucinated function
arguments, and how to guard against them.

</details>

<details>
<summary><strong>Week 8 · Agentic AI — Multi-Agent Systems</strong> (4 hrs) — <em>LO1, LO2, LO3</em></summary>

**Topics**

- When one agent isn't enough: task decomposition and specialist roles
- Multi-agent architectures: supervisor/worker, sequential pipeline, debate/critique patterns
- Frameworks: CrewAI, AutoGen, and LangGraph multi-agent graphs
- Agent-to-agent communication: shared state, message passing, blackboard patterns
- Cost, latency, and reliability trade-offs of multi-agent vs single-agent systems
- Human-in-the-loop checkpoints and approval gates
- Agentic AI risks: prompt injection, runaway actions/cost, cascading errors
- Producing an "agent safety card": scope, tools, oversight, and rollback plan

**Learning Objectives**

- Design a multi-agent system with at least two specialist agents and a coordinator
- Implement a multi-agent workflow using CrewAI or LangGraph for a defined task
- Identify and mitigate prompt injection and cascading-error risks across multiple agents
- Insert a human-in-the-loop approval checkpoint into a multi-agent workflow
- Produce an agent safety card documenting scope, tools, risk, and oversight mechanisms

**Summary**

Most real agentic deployments involve more than one agent. Learners decompose a complex task into
specialist roles (researcher, coder, reviewer) and orchestrate them with CrewAI or a LangGraph
multi-agent graph, comparing supervisor/worker and sequential-pipeline patterns. Responsible AI
content covers prompt injection propagating between agents (demonstrated live), cost-runaway
scenarios unique to multi-agent loops, and human-in-the-loop checkpoints before high-stakes
actions. The agent safety card produced here directly informs the guardrail work in Week 11.

</details>

### Phase 4 — Multimodal AI Systems

<details>
<summary><strong>Week 9 · Multimodal AI: Vision-Language Models</strong> (4 hrs) — <em>LO1, LO2, LO3</em></summary>

**Topics**

- Vision-Language Models (VLMs): CLIP, LLaVA, GPT-4o, Gemini Vision
- CLIP embeddings for zero-shot image classification and semantic image search
- LLaVA and OpenAI Vision API for image understanding and captioning
- Building multimodal pipelines: image → text → structured output
- Industry use-cases: visual QA, document OCR and understanding, accessibility tools
- Evaluating VLM outputs: factual accuracy, hallucination risk, grounding
- Multimodal product design: combining vision and language for real applications

**Learning Objectives**

- Use CLIP embeddings to implement zero-shot image classification without labelled data
- Build a visual question-answering pipeline using a VLM API (GPT-4o or LLaVA)
- Design a multimodal product for a given industry domain
- Evaluate VLM outputs for factual accuracy and hallucination risk
- Construct a multimodal pipeline that processes image input and returns structured output

**Summary**

Learners implement a semantic image-search engine using CLIP embeddings and a FAISS index, then
build a visual QA interface using LLaVA (open-source, Colab-runnable). The session covers how
vision encoders are aligned with language models, and benchmarks open-source (LLaVA) against
commercial (GPT-4o Vision) approaches for accuracy, cost, and deployment suitability. Teams pitch
a multimodal AI product for a given domain in five minutes. Responsible AI considerations include
visual hallucination, accessibility obligations, and bias in vision-language alignment.

</details>

<details>
<summary><strong>Week 10 · Multimodal AI: Speech-to-Text (STT) and Text-to-Speech (TTS)</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- STT fundamentals: acoustic models, language models, CTC and attention decoding
- OpenAI Whisper: architecture, fine-tuning, multilingual capabilities
- HuggingFace speech pipeline: wav2vec 2.0, Whisper API, speech datasets
- Text-to-Speech: neural TTS, VITS, Bark, and the ElevenLabs API
- Building end-to-end voice pipelines: STT → LLM → TTS
- Industry use-cases: voice assistants, transcription, accessibility tools, call-centre AI
- Responsible AI in speech: bias in ASR across accents, speaker privacy, deepfake audio

**Learning Objectives**

- Transcribe audio using OpenAI Whisper and evaluate Word Error Rate (WER) on a test set
- Fine-tune or adapt a Whisper model for a domain-specific vocabulary
- Build a TTS pipeline using a HuggingFace neural TTS model and evaluate naturalness
- Design and implement an end-to-end voice pipeline (STT → LLM → TTS) for a specific use case
- Identify responsible AI risks in speech systems: accent bias, speaker privacy, audio deepfakes

**Summary**

This session completes the multimodal track by adding speech. Learners work with Whisper for STT,
evaluating accuracy across audio conditions and domains, then fine-tune it to a domain-specific
vocabulary. For TTS, learners compare rule-based, neural, and diffusion-based synthesis using
HuggingFace models and the ElevenLabs API. The capstone lab integrates all components: a spoken
question triggers Whisper transcription, an LLM generates an answer, and TTS speaks the response.

</details>

### Phase 5 — Trust, Safety & Guardrails

<details>
<summary><strong>Week 11 · AI Guardrails</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- Why guardrails: the gap between a capable model and a safe production system
- Input guardrails: prompt injection detection, jailbreak pattern detection, PII detection/redaction
- Output guardrails: content moderation (OpenAI Moderation API, Llama Guard), toxicity and hallucination checks
- Guardrail frameworks: NVIDIA NeMo Guardrails and Guardrails AI — programmable rails
- Schema and structured-output validation as a guardrail
- Cost and abuse guardrails: rate limiting, token budgets, and circuit breakers
- Evaluating guardrails: false-positive vs false-negative trade-offs, red-teaming basics
- Human escalation paths: when to hand off from an automated system to a person

**Learning Objectives**

- Implement an input guardrail that detects and blocks a prompt injection attempt
- Implement an output guardrail using a moderation API or a Llama Guard-style classifier
- Configure a rails-based guardrail system (e.g. NeMo Guardrails) for a defined use case
- Evaluate a guardrail configuration for false-positive/false-negative trade-offs on a test set
- Design an escalation path for a production AI system when guardrails are triggered

**Summary**

A capable model is not the same as a safe production system. Learners implement layered guardrails
around an LLM application: input-side prompt-injection and PII detection, output-side moderation
and hallucination checks, using both a programmable rails framework and lightweight schema
validation. A red-teaming lab has learners attempt to break their own (and a peer's) guardrails,
then tune thresholds. The session closes with escalation design — a direct extension of the agent
safety cards from Week 8.

</details>

### Phase 6 — Application Development

<details>
<summary><strong>Week 12 · Media Handling — POSTing Images to a Prediction API, WebRTC</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- REST API fundamentals: HTTP methods, request/response structure, status codes
- Building a prediction API endpoint: Flask/FastAPI serving a trained model
- Handling `multipart/form-data`: uploading images via file inputs to a backend
- POSTing image data from a frontend form to a prediction API
- WebRTC fundamentals: real-time video/audio streams in the browser
- Capturing and sending video frames from a WebRTC stream to an ML model API
- Frontend integration: HTML, JavaScript, and the fetch API for ML-powered web apps

**Learning Objectives**

- Build a REST API endpoint that accepts image uploads and returns model predictions
- Create an HTML form with a file input that POSTs images to a prediction API using `fetch`
- Integrate a WebRTC video stream into a web application and capture frames for inference
- Send real-time video frames from a WebRTC stream to a prediction API and display results
- Debug common integration issues: CORS, file encoding, and API response handling

**Summary**

This session bridges a trained model and a working web application. Learners build a Flask
prediction API that accepts image uploads, then a minimal HTML/JavaScript frontend for upload and
real-time prediction display. The second half introduces WebRTC, enabling live video frame capture
and continuous inference. By the end, learners have a working web app where a user can point their
camera at an object and see live predictions — a compelling portfolio artefact.

</details>

<details>
<summary><strong>Week 13 · Creating a Vue.js App and Connecting to Your ML Model</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- Vue.js fundamentals: components, props, data binding, and lifecycle hooks
- Vue CLI and project structure: scaffolding a production-ready Vue app
- Calling a REST API from Vue.js: axios and the fetch API
- Handling asynchronous requests: async/await, loading states, and error handling
- Building a Vue.js UI for image upload and real-time prediction display
- Connecting the Vue.js frontend to a Flask/FastAPI ML model endpoint
- Deploying a Vue.js + ML backend stack: local development and cloud deployment

**Learning Objectives**

- Scaffold a Vue.js application using Vue CLI and structure components for an ML interface
- Implement image upload, preview, and submission functionality in Vue.js
- Connect a Vue.js frontend to a Flask/FastAPI ML model API using axios
- Handle loading, success, and error states in a Vue.js ML application
- Deploy a full-stack Vue.js + ML API application to a cloud hosting platform

**Summary**

Building on Week 12, this session introduces Vue.js as a production-quality frontend for ML
applications. Learners scaffold a project, build a component-based UI for upload and prediction
display, and connect it to the Flask/FastAPI endpoint from the previous week. The focus is
practical integration: async state, clean display of confidence scores and labels, and edge cases
(invalid file types, API errors, slow inference). The result is a deployable full-stack AI
application — and the foundation for containerisation from Week 14.

</details>

### Phase 7 — Containerised & Agentic Deployment

<details>
<summary><strong>Week 14 · Docker with LLM Models</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- Why containerise LLM fine-tuning: isolating CUDA, PyTorch, and dependency version conflicts
- The Unsloth Docker image: a pre-configured, memory-efficient, GPU-accelerated fine-tuning environment
- Running a GPU-enabled container: the NVIDIA Container Toolkit and `--gpus all`
- Fine-tuning inside the container via bundled Jupyter Lab: LLaMA 3, Mistral, and Gemma templates
- Exporting fine-tuned weights to GGUF for lightweight, dependency-free deployment
- Docker Model Runner: running and querying a GGUF model as an OCI-compliant local artefact
- Exposing a local, OpenAI-compatible inference endpoint from a containerised model
- Comparing this workflow to Week 5's HuggingFace/PEFT pipeline

**Learning Objectives**

- Launch a GPU-enabled Unsloth fine-tuning container with a mounted workspace volume
- Fine-tune an open-source LLM inside the container using a starter notebook template
- Export a fine-tuned model to GGUF format for portable deployment
- Run and query a fine-tuned GGUF model locally using Docker Model Runner
- Connect an external application to a containerised model via its OpenAI-compatible endpoint

**Reference commands**

```bash
# GPU-enabled fine-tuning container with a mounted workspace
docker run --gpus all -it -v "$PWD/workspace:/workspace" -p 8888:8888 unsloth/unsloth

# Run a fine-tuned GGUF artefact locally
docker model run /workspace/my-fine-tuned-model.gguf

# Query it through the local OpenAI-compatible endpoint
curl http://localhost:12434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"my-fine-tuned-model","messages":[{"role":"user","content":"Hello"}]}'
```

**Summary**

Fine-tuning environments are notorious for CUDA/PyTorch version mismatches — Docker removes that
pain by isolating the whole stack. Learners start the official Unsloth image with GPU passthrough
and a mounted volume, fine-tune a LLaMA 3, Mistral, or Gemma model using bundled Jupyter Lab
templates, and export to GGUF. The second half introduces Docker Model Runner for running and
querying the artefact through a local OpenAI-compatible endpoint with no Python dependencies at
inference time. The session closes by comparing the container-first workflow to Week 5's
HuggingFace/PEFT pipeline.

</details>

<details>
<summary><strong>Week 15 · Build and Run Agentic AI Applications with Docker</strong> (4 hrs) — <em>LO2, LO3</em></summary>

**Topics**

- Docker's agentic AI stack: Model Runner, MCP Toolkit/Gateway, and Compose for Agents
- Packaging an agent and its tools as a multi-container Docker Compose application
- The Model Context Protocol (MCP): exposing tools to agents through containerised MCP servers
- Docker MCP Catalog and Gateway: discovering, running, and securing MCP servers in containers
- Sandboxing agent tool execution: isolating code execution and file access per container
- Connecting an agent framework (LangGraph/CrewAI) to a containerised local model and MCP tools
- Observability for containerised agents: logs, traces, and resource limits
- From a local Compose stack to cloud deployment: what changes and what stays the same

**Learning Objectives**

- Define a Docker Compose stack that runs an agent, a local model, and one or more MCP tool servers
- Connect an agent to a containerised MCP tool server and invoke it end-to-end
- Apply container-level sandboxing to limit an agent's file-system and network access
- Configure basic logging/observability for a running agentic application
- Explain the security and isolation benefits of containerising agentic AI tool execution

**Summary**

This session brings together the agentic work from Weeks 7–8, the guardrail thinking from Week 11,
and the containerisation skills from Week 14 into a single deployable stack, following Docker's
official agentic AI workflow. Learners define a Compose application that runs an agent alongside a
local model (via Model Runner) and one or more tool servers exposed through MCP, discovered via
the Docker MCP Catalog and routed through the MCP Gateway. Each tool runs in its own sandboxed
container — a concrete, infrastructure-level guardrail. Learners leave with a fully containerised,
observable agentic application.

Reference: <https://docs.docker.com/guides/agentic-ai>

</details>

### Phase 8 — Career Readiness

<details>
<summary><strong>Week 16 · Performing Interview</strong> (4 hrs) — <em>LO4</em></summary>

**Topics**

- Common AI/ML interview formats: behavioural, technical screen, take-home, live coding, system design
- The STAR method for structuring behavioural answers
- Presenting a portfolio project clearly: problem, approach, trade-offs, results — in under three minutes
- Answering technical follow-ups convincingly: defending your own design decisions
- Handling live coding and whiteboard-style ML system design questions
- Researching the company/role beforehand and preparing questions to ask the interviewer
- Common pitfalls: rambling, overclaiming, and being unable to explain your own code

**Learning Objectives**

- Structure a behavioural answer using the STAR method for a given prompt
- Deliver a three-minute project pitch covering problem, approach, and results
- Answer follow-up technical questions defending design decisions made in a personal project
- Participate in a mock technical interview and receive structured peer/instructor feedback
- Prepare a personalised set of questions to ask an interviewer for a target role

**Summary**

Technical skill only becomes a job offer if a learner can communicate it under interview
conditions. This session runs the full arc of an AI/ML interview: behavioural questions via STAR, a
three-minute capstone pitch, and a live technical follow-up where learners defend specific design
decisions (why LoRA over full fine-tuning, why this vector store, why this guardrail
configuration). A recorded mock-interview lab provides structured feedback on clarity, depth, and
composure.

</details>

<details>
<summary><strong>Week 17 · Projecting a Positive Professional Image</strong> (4 hrs) — <em>LO4</em></summary>

**Topics**

- Personal branding fundamentals: what a hiring manager sees before they meet you
- Building a professional LinkedIn profile: headline, summary, and project descriptions
- Curating a GitHub/portfolio presence: pinned repositories, README quality, and live demo links
- Professional communication etiquette: email, Slack/Teams, and meeting conduct
- Crafting an elevator pitch for networking events and career fairs
- Workplace professionalism: reliability, receiving feedback, and cross-team communication
- Aligning online presence, resume, and interview story into one consistent narrative

**Learning Objectives**

- Audit and improve a LinkedIn profile against a professional-presence checklist
- Curate a GitHub portfolio with clear READMEs and a highlighted flagship project
- Draft a 30-second elevator pitch for a networking or career-fair context
- Write a professional email/Slack message appropriate to a workplace scenario
- Produce a consistency check across resume, LinkedIn, portfolio, and interview narrative

**Summary**

The course closes by turning a semester of technical work into a coherent professional identity.
Learners audit and rewrite their LinkedIn profile, curate a GitHub portfolio around their strongest
project (clear README, live demo link where possible), and draft a 30-second elevator pitch. A
workplace-etiquette segment covers professional communication and receiving feedback. The session
ends with a consistency audit: resume, LinkedIn, portfolio, and interview story should all tell the
same story about the same person.

</details>

---

## Learning Outcome Coverage Matrix

| Week | Topic | LO1 | LO2 | LO3 | LO4 |
|------|-------|:---:|:---:|:---:|:---:|
| 1 | Design Thinking for AI Product Development | ✅ | ✅ | | |
| 2 | Vibe Programming: Spec-Driven Development | ✅ | ✅ | | |
| 3 | AI Ethics and Governance Overview | ✅ | ✅ | | |
| 4 | Model Optimisation with ONNX | | ✅ | ✅ | |
| 5 | Fine-Tuning, LoRA & HuggingFace Pipelines | | ✅ | ✅ | |
| 6 | Retrieval-Augmented Generation (RAG) | ✅ | ✅ | ✅ | |
| 7 | Agentic AI — Single-Agent Systems | ✅ | ✅ | ✅ | |
| 8 | Agentic AI — Multi-Agent Systems | ✅ | ✅ | ✅ | |
| 9 | Multimodal AI: Vision-Language Models | ✅ | ✅ | ✅ | |
| 10 | Multimodal AI: STT and TTS | | ✅ | ✅ | |
| 11 | AI Guardrails | | ✅ | ✅ | |
| 12 | Media Handling: Prediction API & WebRTC | | ✅ | ✅ | |
| 13 | Vue.js App Connected to an ML Model | | ✅ | ✅ | |
| 14 | Docker with LLM Models | | ✅ | ✅ | |
| 15 | Agentic AI Applications with Docker | | ✅ | ✅ | |
| 16 | Performing Interview | | | | ✅ |
| 17 | Projecting a Positive Professional Image | | | | ✅ |

---

## Technology Stack

| Area | Tools & Platforms |
|------|-------------------|
| **Core DL** | PyTorch, TensorFlow, HuggingFace `transformers` / `datasets` / `evaluate` / `accelerate` |
| **Optimisation** | ONNX, ONNX Runtime, INT8/FP16 quantisation (TensorRT & OpenVINO positioned comparatively) |
| **Fine-tuning** | PEFT (LoRA, QLoRA), Unsloth, GGUF |
| **Experiment tracking** | Weights & Biases, MLflow Model Registry, HuggingFace Hub |
| **GenAI / RAG** | LangChain, LlamaIndex, FAISS, Chroma, Pinecone, sentence-transformers, RAGAs |
| **Agentic AI** | LangGraph, CrewAI, AutoGen, Model Context Protocol (MCP), Pydantic |
| **Multimodal** | CLIP, LLaVA, GPT-4o Vision, Whisper, wav2vec 2.0, VITS, Bark, ElevenLabs |
| **Guardrails** | NVIDIA NeMo Guardrails, Guardrails AI, Llama Guard, OpenAI Moderation API |
| **Application** | Flask, FastAPI, Vue.js, axios, WebRTC, REST / `multipart/form-data` |
| **Deployment** | Docker, Docker Compose, Docker Model Runner, Docker MCP Catalog & Gateway, NVIDIA Container Toolkit |
| **AI-assisted dev** | Claude Code, GitHub Copilot, Cursor, GitHub Spec Kit |
| **Governance** | Singapore Model AI Governance Framework, IMDA/AI Verify, AI BoK, GDPR/PDPA |

---

## Repository Structure

> **Note — intentional omission:** the source curriculum document specifies syllabus content only.
> The layout below is a *suggested* teaching-repository structure, not part of the approved
> curriculum. Adjust or delete it to match the actual repository.

```
.
├── README.md
├── week-01-design-thinking/
├── week-02-spec-driven-development/
├── week-03-ai-ethics-governance/
├── week-04-onnx-optimisation/
├── week-05-lora-huggingface/
├── week-06-rag-systems/
├── week-07-agentic-single/
├── week-08-agentic-multi/
├── week-09-vision-language-models/
├── week-10-speech-stt-tts/
├── week-11-ai-guardrails/
├── week-12-media-api-webrtc/
├── week-13-vuejs-ml-app/
├── week-14-docker-llm/
├── week-15-docker-agentic/
├── week-16-interview-prep/
├── week-17-professional-image/
└── capstone/
```

Each week folder is expected to hold its notebooks, slides, lab instructions, datasets or data
pointers, and solution code.

---

## Getting Started

> **Note — intentional omission:** the source curriculum document does not define environment
> setup, hardware provisioning, or assessment weighting. The guidance below reflects the tooling
> named in the syllabus and should be confirmed against the module's official delivery plan.

**Compute**

- Weeks 5, 9, 10: free-tier Google Colab (T4 GPU) is sufficient for the specified labs.
- Weeks 14–15: a local or cloud machine with an NVIDIA GPU, Docker Engine, and the NVIDIA
  Container Toolkit installed.

**Accounts / API keys likely required**

- HuggingFace Hub, Weights & Biases, an LLM provider (OpenAI and/or Anthropic), and ElevenLabs
  (Week 10). Store keys in a local `.env` file; never commit them.

**Suggested baseline environment**

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U torch transformers datasets evaluate accelerate peft \
    onnx onnxruntime langchain langgraph chromadb sentence-transformers \
    ragas wandb fastapi uvicorn
```

Pin exact versions per week in that week's own `requirements.txt`.

---

## Contributing

Contributions are welcome — corrections to lab instructions, updated library versions, additional
worked examples, or improved datasets. Please open an issue describing the change before
submitting a pull request, and keep each PR scoped to a single week where possible.

---

## Licence

> **Note — intentional omission:** no licence is specified in the source curriculum document.
> Add the appropriate licence (institutional or open-source) before publishing this repository.

---

<sub>AI Innovation with Deep Learning · 17-Week Industry Curriculum · Revised Edition</sub>
