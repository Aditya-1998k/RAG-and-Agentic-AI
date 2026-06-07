# Setup
import chromadb
from chromadb.utils import embedding_functions
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Collection creation
client = chromadb.Client()
collection = client.create_collection(
    name="my_collection_name",
    metadata={"topic": "query testing"},
    configuration={
        "hnsw": {
            "space": "cosine",
            "ef_search": 100,
            "ef_construction": 100,
            "max_neighbors": 16
        },
        "embedding_function": ef
    }
)

collection.add(
    documents=[
        "Giant pandas are a bear species that lives in mountainous areas.",
        "A pandas DataFrame stores two-dimensional, tabular data",
        "I think everyone agrees that pandas are some of the cutest animals on the planet",
        "A direct comparison between pandas and polars indicates that polars is a more efficient library than pandas.",
    ],
    metadatas=[
        {"topic": "animals"},
        {"topic": "data analysis"},
        {"topic": "animals"},
        {"topic": "data analysis"},
    ],
    ids=["id1", "id2", "id3", "id4"]
)


# Querying text for nearest neighbors
result = collection.query(
    query_texts=["cats"],
    n_results=10,
)

print("Results for 'cats':", result)

# Querying text for nearest neighbors
result = collection.query(
    query_texts=["polar bear"],
    n_results=1,
)

print("Results for 'polar bear':", result)

# Querying text for nearest neighbors with metadata filtering
result = collection.query(
    query_texts=["polar bear"],
    n_results=1,
    where={'topic': 'animals'}
)

print("Results for 'polar bear' with metadata filtering:", result)

# Querying text for nearest neighbors with Document filtering
result = collection.query(
    query_texts=["polar bear"],
    n_results=1,
    where_document={'$not_contains': 'library'}
)
print("Results for 'polar bear' with document filtering:", result)

# Querying text for nearest neighbors with metadata filtering and Document filtering
result = collection.query(
    query_texts=["polar bear"],
    n_results=1,
    where={'topic': 'animals'},
    where_document={'$not_contains': 'library'}
)
print("Results for 'polar bear' with both filtering:", result)