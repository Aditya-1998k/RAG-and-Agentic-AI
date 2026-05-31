from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    SimpleDirectoryReader
)
from rag.embedding.gemini import GeminiEmbedding
from rag.vectorstores.chroma import ChromaStore
from .chunker import Chunker

class IngestionPipeline:

    def run(self, path: str):

        docs = (
            SimpleDirectoryReader(
                path
            ).load_data()
        )

        parser = Chunker.get()

        nodes = parser.get_nodes_from_documents(
            docs
        )

        vector_store = (
            ChromaStore().get_store()
        )

        storage_context = (
            StorageContext.from_defaults(
                vector_store=vector_store
            )
        )

        VectorStoreIndex(
            nodes=nodes,
            storage_context=storage_context,
            embed_model=GeminiEmbedding().get_model()
        )