# 🍽️ AI Food Recommendation System

A Retrieval-Augmented Generation (RAG) powered food recommendation system built using:

* Google Gemini 2.5 Flash
* ChromaDB
* Hugging Face Embeddings (BGE)
* Semantic Search
* Metadata Filtering
* Conversational AI

This project demonstrates three approaches to information retrieval and recommendation:

1. Interactive Search
2. Advanced Filtered Search
3. Gemini-Powered RAG Chatbot

---

# Features

## Interactive Search

Perform semantic food search using natural language.

Examples:

```text
chocolate dessert
healthy breakfast
spicy dinner
italian food
```

Features:

* Semantic similarity search
* Top recommendation highlighting
* Search history tracking
* Related search suggestions

---

## Advanced Search
Search using metadata filters.
Supported filters:

* Cuisine Type
* Maximum Calories
* Cooking Method
* Combined Filters

Examples:

```text
healthy meal
Cuisine: Italian
```

```text
dessert
Calories < 300
```

```text
protein rich meal
Cooking Method: Grilling
```

---

## Gemini RAG Chatbot

Uses Retrieval-Augmented Generation.

Workflow:

```text
User Query
     │
     ▼
ChromaDB Search
     │
     ▼
Relevant Food Documents
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Context-Aware Response
```

Examples:

```text
1. I want something healthy and light for lunch
2. Suggest a spicy dinner option
3. What are some low calorie desserts?
```

---

# Project Structure

```text
food-recommendation-system/
│
├── FoodDataSet.json
│
├── chroma_db/
│
├── shared_functions.py
│
├── interactive_search.py
│
├── advanced_search.py
│
├── enhanced_rag_chatbot.py
│
├── system_comparison.py
│
├── requirements.txt
│
└── README.md
```

---

# Technology Stack

| Component       | Technology                     |
| --------------- | ------------------------------ |
| Vector Database | ChromaDB                       |
| Embeddings      | BAAI/bge-base-en-v1.5          |
| LLM             | Gemini 2.5 Flash               |
| Language        | Python                         |
| Search          | Semantic Similarity Search     |
| AI Technique    | Retrieval-Augmented Generation |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/food-recommendation-system.git
cd food-recommendation-system
```
---

## Create Virtual Environment
Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```
Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```text
chromadb
sentence-transformers
google-genai
numpy
python-dotenv
```

---

# Environment Variables
Create a `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key
```
Or export directly:
Linux/macOS:
```bash
export GEMINI_API_KEY=your_api_key
```

Windows:
```powershell
set GEMINI_API_KEY=your_api_key
```

---

# Dataset

Source: [Data source Link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/sN1PIR8qp1SJ6K7syv72qQ/FoodDataSet.json)

---
The system uses a food dataset containing:

* Food Name
* Description
* Ingredients
* Cuisine Type
* Calories
* Health Benefits
* Cooking Method
* Taste Profile

Example:

```json
{
  "food_name": "Apple Pie",
  "food_description": "Classic baked dessert",
  "cuisine_type": "American",
  "food_calories_per_serving": 320,
  "food_ingredients": [
    "Apples",
    "Flour",
    "Sugar"
  ]
}
```

---

# Embedding Model

This project uses:

```text
BAAI/bge-base-en-v1.5
```

Advantages:

* Strong retrieval performance
* Free and open source
* Fast inference
* Excellent semantic understanding

---

# ChromaDB Persistence

The project uses:

```python
chromadb.PersistentClient(
    path="./chroma_db"
)
```

Benefits:

* Embeddings generated only once
* No re-indexing on every restart
* Faster startup time
* Persistent vector storage

Startup behavior:

```text
First Run
─────────────
Create Collection
Generate Embeddings
Store Vectors

Subsequent Runs
─────────────
Open Existing Collection
Reuse Stored Embeddings
Skip Re-Indexing
```

---

# Running Interactive Search

```bash
python interactive_search.py
```

Example:

```text
🔍 Search food:

healthy breakfast
```

Result:

```text
1. Greek Yogurt Bowl
2. Oatmeal with Berries
3. Avocado Toast
```

---

# Running Advanced Search

```bash
python advanced_search.py
```

Features:

```text
1. Basic Search
2. Cuisine Search
3. Calorie Search
4. Cooking Method Search
5. Combined Filters
```

Example:

```text
healthy meal
Cuisine: Mediterranean
Calories: 400
```

---

# Running Gemini RAG Chatbot

```bash
python enhanced_rag_chatbot.py
```

Example Query:

```text
I want something healthy for lunch
```

Example Response:

```text
I recommend the Mediterranean Grilled Chicken Salad.

It is high in protein, rich in vegetables,
and contains approximately 280 calories,
making it an excellent lunch option.
```

---

# Comparison Mode

Inside chatbot:

```text
compare
```
Example:
```text
Query 1:
chocolate dessert
Query 2:
healthy breakfast
```

Gemini generates an AI-powered comparison.

---

# System Comparison

Run:
```bash
python system_comparison.py
```

Compares:

1. Interactive Search
2. Advanced Search
3. Gemini RAG Chatbot

Metrics:

* Retrieval Quality
* Response Style
* Search Accuracy
* User Experience

---

# Architecture

```text
                   User Query
                        │
                        ▼
              Similarity Search
                        │
                        ▼
                 ChromaDB
                        │
                        ▼
          BGE Embedding Retrieval
                        │
                        ▼
             Relevant Food Items
                        │
                        ▼
              Gemini 2.5 Flash
                        │
                        ▼
              Natural Response
```

---

# Learning Objectives

This project demonstrates:

* Vector Databases
* ChromaDB
* Embeddings
* Semantic Search
* Metadata Filtering
* Retrieval-Augmented Generation
* Prompt Engineering
* Conversational AI
* Gemini API Integration

---

# Future Improvements

Potential enhancements:

* FastAPI Backend
* Gradio UI
* Streamlit Dashboard
* User Preference Memory
* Meal Planning
* Nutrition Analysis
* Multi-Turn Conversation Memory
* Food Image Search
* Recipe Generation

---

# License

Apache 2.0

This project is based on the CognitiveClass AI Food Search and RAG Chatbot practice project and has been extended with Gemini, ChromaDB persistence, and improved retrieval capabilities.
