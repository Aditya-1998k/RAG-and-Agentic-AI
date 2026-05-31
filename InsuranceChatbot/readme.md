# RAG Platform

A production-oriented Retrieval-Augmented Generation (RAG) application built using **Python**, **FastAPI**, **LlamaIndex**, **ChromaDB**, **Hugging Face Embeddings**, **Ollama**, and **Gradio**.

The project is designed with modular components so that vector stores, embedding models, and LLMs can be replaced with minimal code changes.

---

# Features

* Document ingestion through REST APIs
* PDF and text document support
* Local embeddings using BGE Small
* Local LLM inference using Ollama
* ChromaDB vector storage
* FastAPI backend APIs
* Gradio chat interface
* Source-aware retrieval
* Context-only answering guardrails
* Modular project structure
* Swagger/OpenAPI documentation

---

# Architecture

```text
                ┌─────────────┐
                │  Gradio UI  │
                └──────┬──────┘
                       │
                       ▼

                ┌─────────────┐
                │   FastAPI   │
                └──────┬──────┘
                       │
                       ▼

                ┌─────────────┐
                │ RAG Service │
                └──────┬──────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼

 ┌─────────────┐              ┌─────────────┐
 │ Retriever   │              │ Ollama LLM  │
 └──────┬──────┘              └─────────────┘
        │
        ▼

 ┌─────────────┐
 │ ChromaDB    │
 └──────┬──────┘
        │
        ▼

 ┌─────────────┐
 │ BGE Small   │
 │ Embeddings  │
 └─────────────┘
```

---

# Technology Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| Backend API     | FastAPI                |
| UI              | Gradio                 |
| RAG Framework   | LlamaIndex             |
| Vector Database | ChromaDB               |
| Embeddings      | BAAI/bge-small-en-v1.5 |
| LLM             | Qwen2.5 via Ollama     |
| Language        | Python                 |

---

# Project Structure

```text
rag-platform/

├── main.py
├── ui.py
│
├── api/
│   └── routes/
│       ├── ingest.py
│       ├── query.py
│       └── health.py
│
├── core/
│   ├── config.py
│   ├── logger.py
│   └── exceptions.py
│
├── rag/
│   │
│   ├── llms/
│   │   ├── base.py
│   │   └── ollama.py
│   │
│   ├── embedding/
│   │   ├── base.py
│   │   └── huggingface.py
│   │
│   ├── vectorstores/
│   │   ├── base.py
│   │   └── chroma.py
│   │
│   ├── ingestion/
│   │   ├── pipeline.py
│   │   ├── chunker.py
│   │   └── metadata.py
│   │
│   ├── retrival/
│   │   ├── retrieval.py
│   │   ├── reranker.py
│   │   └── hybrid.py
│   │
│   └── service.py
│
├── data/
│
├── chroma_db/
│
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>

cd rag-platform
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

Start Ollama:

```bash
ollama serve
```

Pull Qwen model:

```bash
ollama pull qwen2.5:3b
```

Verify:

```bash
ollama list
```

---

# Environment Variables

Create `.env`

```env
VECTOR_DB_PATH=./chroma_db
CHROMA_COLLECTION=documents
TOP_K=5
```

---

# Running the Backend

Start FastAPI:

```bash
uvicorn main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Running Gradio UI

Start backend first.

Open another terminal:

```bash
python ui.py
```

Open:

```text
http://localhost:7860
```

---

# Document Ingestion

Upload PDF using:

```http
POST /ingest
```

or place documents inside:

```text
data/
```

Supported formats:

* PDF
* TXT
* DOCX
* Markdown
* CSV
* HTML

---

# Query Endpoint

```http
POST /query
```

---

# Guardrails

The application includes basic RAG guardrails.

Rules:

* Answer only from retrieved context
* Do not use model knowledge
* Do not hallucinate
* Reject unsupported questions
* Return fallback response when answer is unavailable

Fallback response:

```text
I could not find the answer in the provided documents.
```

Prompt enforcement:

```text
1. Answer ONLY from context.
2. Do NOT make assumptions.
3. Do NOT use external knowledge.
4. If answer is not found, return fallback response.
```

---

# Sample Dataset

Create:

```text
data/company_story.txt
```

Content:

```text
Acme Technologies was founded in 2018 by Rahul Sharma and Priya Mehta in Bengaluru, India.
The company specializes in cloud-native software solutions for healthcare organizations.
In 2019, Acme Technologies launched its first product, HealthFlow.
In 2020, the company expanded to Bengaluru, Hyderabad, and Pune and hired its first 50 employees.
In March 2021, Acme secured Series A funding of $5 million from Horizon Ventures.
In 2022, the company launched MedInsight.
By 2023, Acme was serving over 200 hospitals across India and processing approximately 10 million patient records annually.
The company received the Healthcare Innovation Award in 2024.
As of 2025, Acme employs 350 people and maintains offices in Bengaluru, Hyderabad, Pune, and Chennai.
Rahul Sharma serves as CEO and Priya Mehta serves as CTO.
The long-term vision of the company is to use AI and cloud computing to improve healthcare accessibility across Asia.
```

---

# Sample Questions

## Basic Retrieval

```text
Who founded Acme Technologies?
When was Acme Technologies founded?
What was the first product launched by Acme?
Who is the CEO?
Who is the CTO?
What is MedInsight?
```

---

# Embedding Model

```text
BAAI/bge-small-en-v1.5
```

Benefits:

* Free
* Runs locally
* Fast
* Good retrieval quality
* No API costs

---

# LLM Model

```text
qwen2.5:3b
```

Benefits:

* Local inference
* Small memory footprint
* Good instruction following
* Suitable for RAG

---

# Development Roadmap

## Phase 1

* [x] FastAPI
* [x] ChromaDB
* [x] Ollama
* [x] BGE Embeddings
* [x] Gradio UI

