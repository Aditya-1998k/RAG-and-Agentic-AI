# Employee Semantic Search with ChromaDB

A modular Python application that demonstrates how to build a semantic employee search engine using ChromaDB and Sentence Transformers.

The application stores employee profiles as vector embeddings and supports:

* Semantic similarity search
* Metadata filtering
* Combined vector + metadata search
* Modular and scalable architecture
* Easy migration to production vector databases

---

# Features

## Semantic Search

Search employees using natural language queries.

Examples:

* Python developer with web development experience
* Senior engineering leader
* DevOps engineer with Kubernetes knowledge
* Marketing specialist with analytics experience

---

## Metadata Filtering

Filter employees based on structured fields:

* Department
* Experience
* Location
* Employment Type
* Role

Examples:

```python
where={"department": "Engineering"}

where={"experience": {"$gte": 10}}

where={"location": {"$in": ["San Francisco", "New York"]}}
```

---

## Combined Search

Perform semantic search while applying metadata constraints.

Example:

```python
search_service.semantic_search(
    query="senior Python developer",
    n_results=5,
    where={
        "$and": [
            {"experience": {"$gte": 8}},
            {"location": {"$in": ["Seattle", "San Francisco"]}
        ]
    }
)
```

---

# Project Structure

```text
employee-search/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── data/
│   └── employees.py
│
├── embeddings/
│   └── embedding_factory.py
│
├── database/
│   ├── chroma_client.py
│   └── collection_manager.py
│
├── services/
│   ├── employee_service.py
│   └── search_service.py
│
├── models/
│   └── employee.py
│
├── utils/
│   └── logger.py
│
└── tests/
    └── test_search.py
```

---

# Architecture

```text
                 ┌─────────────────┐
                 │     app.py      │
                 └────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Application Layer │
                └────────┬─────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 ┌─────────────────┐         ┌─────────────────┐
 │ EmployeeService │         │ SearchService   │
 └────────┬────────┘         └────────┬────────┘
          │                           │
          ▼                           ▼
 ┌──────────────────────────────────────────┐
 │            Chroma Collection             │
 └──────────────────────────────────────────┘
                         │
                         ▼
 ┌──────────────────────────────────────────┐
 │ SentenceTransformer Embeddings           │
 │ all-MiniLM-L6-v2                         │
 └──────────────────────────────────────────┘
```

---

# Technologies Used

| Component         | Technology            |
| ----------------- | --------------------- |
| Vector Database   | ChromaDB              |
| Embeddings        | Sentence Transformers |
| Language          | Python 3.10+          |
| Similarity Metric | Cosine Similarity     |
| Data Model        | Dataclasses           |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/employee-search.git

cd employee-search
```

---

## Create Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
chromadb
sentence-transformers
torch
numpy
```

Install manually:

```bash
pip install chromadb sentence-transformers torch numpy
```

---

# Running the Application

```bash
python app.py
```

Expected output:

```text
Collection created: employee_collection

Searching for Python developers...

1. John Doe
2. Alex Rodriguez
3. Michael Brown
```

---

# Example Searches

## Python Developers

```python
search_service.semantic_search(
    query="Python developer with web development experience",
    n_results=3
)
```

---

## Leadership Roles

```python
search_service.semantic_search(
    query="engineering manager and technical leader",
    n_results=3
)
```

---

## Engineering Employees

```python
search_service.filter_by_department(
    "Engineering"
)
```

---

## Employees With 10+ Years Experience

```python
search_service.filter_by_experience(
    10
)
```

---

## Employees In California

```python
search_service.filter_by_location(
    ["San Francisco", "Los Angeles"]
)
```

---

# Employee Document Format

Each employee profile is transformed into a semantic document before indexing.

Example:

```text
Software Engineer with 5 years of experience in Engineering.
Skills: Python, JavaScript, React, Node.js, databases.
Located in New York.
Employment type: Full-time.
```

These documents are embedded into vectors and stored inside ChromaDB.

---

# Future Enhancements

## REST API

Expose search functionality using FastAPI.

```text
POST /employees/search
GET  /employees
GET  /employees/{id}
```

---

## Persistent Chroma Storage

Current implementation uses in-memory storage.

Upgrade to persistent storage:

```python
chromadb.PersistentClient(path="./chroma_db")
```

---

## Hybrid Search

Combine:

* Semantic Search
* Keyword Search
* Metadata Filtering

For improved relevance.

---

## LLM Integration

Integrate with:

* LangChain
* LlamaIndex
* OpenAI
* Gemini
* Ollama

Example use case:

```text
Find senior Python developers experienced in Kubernetes
and summarize their strengths.
```

---

## Migration To Production Vector Databases

The architecture can easily be migrated to:

* ChromaDB
* Qdrant
* Pinecone
* Weaviate
* Milvus
* Elasticsearch Vector Search

without changing business logic.

---

# Learning Objectives

This project helps understand:

* Embeddings
* Vector Databases
* Semantic Search
* Similarity Search
* Metadata Filtering
* Hybrid Retrieval
* RAG Fundamentals
* Clean Architecture
* Service Layer Design

---

# License

MIT License

Feel free to use, modify, and extend this project for learning or production purposes.
