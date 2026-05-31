from llama_index.embeddings.huggingface import HuggingFaceEmbedding


class HuggingFaceEmbeddingModel:

    def get_model(self):
        return HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )