from chromadb.utils import embedding_functions
from config.settings import EMBEDDING_MODEL


def get_embedding_function():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
