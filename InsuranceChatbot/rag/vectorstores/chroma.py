import chromadb
from llama_index.vector_stores.chroma import (
    ChromaVectorStore
)
from core.config import settings
from .base import BaseVectorStore


class ChromaStore(BaseVectorStore):

    def get_store(self):

        client = chromadb.PersistentClient(
            path=settings.VECTOR_DB_PATH
        )

        collection = (
            client.get_or_create_collection(
                settings.CHROMA_COLLECTION
            )
        )

        return ChromaVectorStore(
            chroma_collection=collection
        )