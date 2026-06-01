from llama_index.llms.google_genai import GoogleGenAI

from core.config import settings
from .base import BaseLLM


class GeminiLLM(BaseLLM):
    """Gemini LLM implementation."""

    def __init__(self):
        self.client = GoogleGenAI(
            model="gemini-2.5-flash",
            api_key=settings.GEMINI_API_KEY,
        )

    def generate(self, prompt: str) -> str:
        response = self.client.complete(prompt)
        return response.text