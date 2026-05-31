from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

from core.config import settings
from .base import BaseEmbedding

class GeminiEmbedding(BaseEmbedding):
    """Gemini embedding implementation."""

    def get_model(self):
        return GoogleGenAIEmbedding(
            model_name="gemini-embedding-002",
            api_key=settings.GEMINI_API_KEY
        )