# RAG Platform

A production-oriented Retrieval-Augmented Generation (RAG) application built using **Python**, **FastAPI**, **LlamaIndex**, **Google Gemini**, and **ChromaDB**.

The project is designed with extensibility in mind, allowing future integration of additional LLMs, embedding providers, and vector databases.

---

## Features

* Document ingestion through REST API
* PDF document support
* Automatic chunking using LlamaIndex
* Gemini Embeddings (`text-embedding-004`)
* ChromaDB persistent vector storage
* Gemini LLM for response generation
* FastAPI-based REST APIs
* Modular architecture for future expansion
* Swagger/OpenAPI documentation

---

## Tech Stack

| Component       | Technology        |
| --------------- | ----------------- |
| API Framework   | FastAPI           |
| LLM             | Gemini            |
| Embeddings      | Gemini Embeddings |
| Vector Database | ChromaDB          |
| RAG Framework   | LlamaIndex        |
| Language        | Python 3.11+      |

---

## Project Structure

```text
rag-platform/

├── main.py
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
│   │   ├── gemini.py
│   │   └── openai.py
│   │
│   ├── embeddings/
│   │   ├── base.py
│   │   ├── gemini.py
│   │   └── hf.py
│   │
│   ├── vectorstores/
│   │   ├── base.py
│   │   ├── chroma.py
│   │   └── qdrant.py
│   │
│   ├── ingestion/
│   │   ├── pipeline.py
│   │   ├── chunker.py
│   │   └── metadata.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
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
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>

cd rag-platform
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key

VECTOR_DB_PATH=./chroma_db

CHROMA_COLLECTION=documents

TOP_K=5
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

OpenAPI Schema:

```text
http://localhost:8000/openapi.json
```

---

## Document Ingestion

The document is:

1. Uploaded to the `data/` directory
2. Parsed by LlamaIndex
3. Chunked using SentenceSplitter
4. Embedded using Gemini Embeddings
5. Stored in ChromaDB

Example Response:

```json
{
  "message": "document indexed",
  "file": "AWS_Guide.pdf"
}
```

---

## Querying Documents

Endpoint:

```http
POST /query
```

Request:

```json
{
  "question": "What is AWS Lambda?"
}
```

Response:

```json
{
  "answer": "AWS Lambda is a serverless compute service..."
}
```

---

## RAG Workflow

```text
User Query
    │
    ▼

Retriever
    │
    ▼

ChromaDB
    │
    ▼

Relevant Chunks
    │
    ▼

Gemini LLM
    │
    ▼

Generated Answer
```

---

## Supported Documents

Current support:

* PDF
* TXT
* Markdown
* DOCX
* HTML
* CSV

Supported through LlamaIndex document readers.

---

## Future Enhancements

### Retrieval

* Hybrid Search
* BM25 Search
* Metadata Filtering
* Multi-Vector Retrieval

### Ranking

* Cohere Reranker
* Jina Reranker
* BGE Reranker

### Vector Databases

* Qdrant
* pgvector
* Weaviate
* Pinecone

### LLM Providers

* OpenAI
* Anthropic Claude
* Ollama
* Azure OpenAI

### Production Features

* JWT Authentication
* RBAC
* Multi-tenancy
* OpenTelemetry
* Prometheus Metrics
* Grafana Dashboards
* CI/CD Pipelines
* Docker
* Kubernetes
* Terraform

---

## Development Roadmap

### Phase 1

* [x] FastAPI Setup
* [x] PDF Upload
* [x] Gemini Embeddings
* [x] ChromaDB
* [x] Basic Query Endpoint
