# RAG and Agentic AI Projects

A collection of projects exploring Retrieval-Augmented Generation (RAG) and Agentic AI architectures, demonstrating practical implementations of LLM-powered applications with advanced retrieval and reasoning capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a series of projects that implement modern AI architectures including:

- **Retrieval-Augmented Generation (RAG)**: Combining vector databases with LLMs for context-aware responses
- **Agentic AI**: Building autonomous agents that reason, plan, and execute tasks
- **Multi-LLM Support**: Flexible implementations supporting multiple LLM providers
- **Advanced Retrieval**: Hybrid search, reranking, and intelligent document chunking

Each project is self-contained while sharing common patterns and utilities for RAG and agentic AI implementations.

## 📁 Projects

### InsuranceChatbot
A RAG-based chatbot system that answers insurance-related queries using domain-specific documents.

**Key Features:**
- Document ingestion and embedding with multiple provider support
- Hybrid retrieval combining BM25 and semantic search
- Document reranking for improved relevance
- Multi-LLM support (Gemini, Ollama) with factory pattern
- FastAPI REST endpoints

**Location:** `./InsuranceChatbot/`

More projects coming soon...

## 🏗️ Architecture

### Core Components

1. **RAG Service** - Orchestrates retrieval and generation
2. **Retrieval Module** - Handles document search and ranking
3. **Embedding Module** - Manages vector embeddings from multiple providers
4. **LLM Module** - Factory-based LLM instantiation
5. **Vector Store** - Chroma-based vector database
6. **API Routes** - FastAPI endpoints for ingestion and querying

### Technology Stack

- **Vector Database:** Chroma
- **LLM Frameworks:** LlamaIndex
- **LLM Providers:** Gemini, Ollama
- **Embeddings:** Hugging Face, Gemini
- **API Framework:** FastAPI
- **Database:** SQLite (metadata storage)

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment manager (venv recommended)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd RAG-and-Agentic-AI
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the project root (or specific project directories):

```env
# LLM Configuration
LLM_PROVIDER=ollama              # Options: "gemini" or "ollama"
GEMINI_API_KEY=your_api_key_here

# Vector Database
VECTOR_DB_PATH=./chroma_db
CHROMA_COLLECTION=documents

# Retrieval
TOP_K=5
```

**Environment Variables:**
- `LLM_PROVIDER`: Choose between "gemini" (requires API key) or "ollama" (local)
- `GEMINI_API_KEY`: Your Google Gemini API key (only if using Gemini)
- `VECTOR_DB_PATH`: Path to Chroma database directory
- `CHROMA_COLLECTION`: Collection name in Chroma
- `TOP_K`: Number of documents to retrieve

## 📂 Project Structure

```
RAG-and-Agentic-AI/
├── README.md
├── requirements.txt
├── .env.example
│
├── InsuranceChatbot/
│   ├── main.py                 # FastAPI application
│   ├── ui.py                   # UI components
│   ├── requirements.txt
│   ├── readme.md
│   │
│   ├── api/
│   │   ├── models/             # Request/response models
│   │   └── routes/             # API endpoints
│   │
│   ├── core/
│   │   └── config.py           # Configuration management
│   │
│   ├── rag/
│   │   ├── service.py          # RAG orchestration
│   │   ├── embedding/          # Embedding providers
│   │   ├── ingestion/          # Document processing
│   │   ├── llms/               # LLM factory and implementations
│   │   ├── retrival/           # Retrieval and reranking
│   │   └── vectorstores/       # Vector database interfaces
│   │
│   ├── data/                   # Sample documents
│   └── chroma_db/              # Vector database storage
│
└── [Additional projects...]
```

## 🔧 Key Features

### Factory Pattern LLM Selection
Dynamically select LLM providers via configuration without code changes:
```python
# Automatically selected based on LLM_PROVIDER config
llm = LLMFactory.create_llm()
```

### Multi-Provider Support
- **Embeddings:** Hugging Face, Gemini
- **LLMs:** Gemini (cloud), Ollama (local)
- **Vector Stores:** Chroma

### Hybrid Retrieval
Combines multiple search strategies for better results:
- Semantic search via embeddings
- BM25 keyword search
- Document reranking

## 📚 Technologies

| Component | Technology |
|-----------|-----------|
| Vector DB | Chroma |
| LLM Framework | LlamaIndex |
| LLM Providers | Google Gemini, Ollama |
| Embeddings | Hugging Face, Google Gemini |
| API | FastAPI |
| Config | Pydantic Settings |
| Storage | SQLite, Chroma Storage |

## 🚦 Running Projects

### InsuranceChatbot

1. **Navigate to project:**
   ```bash
   cd InsuranceChatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file** with your configuration

4. **Ingest documents:**
   ```bash
   # Via API
   curl -X POST "http://localhost:8000/ingest" \
     -H "Content-Type: application/json" \
     -d '{"file_path": "data/story.txt"}'
   ```

5. **Query documents:**
   ```bash
   # Via API
   curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is insurance?"}'
   ```

6. **Run application:**
   ```bash
   # FastAPI server
   python main.py
   
   # Or with Uvicorn
   uvicorn main:app --reload
   ```

## 🔄 Switching LLM Providers

Change the `LLM_PROVIDER` in your `.env` file:

```env
# Use Gemini (requires API key)
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here

# Or use Ollama (local)
LLM_PROVIDER=ollama
```

No code changes needed - the factory pattern handles provider switching.

## 🤝 Contributing

Contributions are welcome! When adding new projects:

1. Create a new directory following the existing structure
2. Include comprehensive README with setup instructions
3. Follow the factory pattern for extensible components
4. Document any new dependencies in requirements.txt
5. Maintain consistency with existing code style

## 📝 License

This repository is for educational purposes.

## 📞 Contact & Resources

- RAG Documentation: [LlamaIndex Docs](https://docs.llamaindex.ai/)
- Vector DB: [Chroma Docs](https://docs.trychroma.com/)
- LLM Provider: [Google Gemini Docs](https://ai.google.dev/)
