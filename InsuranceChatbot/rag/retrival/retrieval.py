from llama_index.core import VectorStoreIndex

from rag.embedding.gemini import GeminiEmbedding
from rag.vectorstores.chroma import ChromaStore

class Retriever:

    def get(self):

        index = (
            VectorStoreIndex.from_vector_store(
                vector_store=ChromaStore().get_store(),
                embed_model=GeminiEmbedding().get_model()
            )
        )

        return index.as_retriever(
            similarity_top_k=5
        )
