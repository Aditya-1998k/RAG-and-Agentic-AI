from llama_index.llms.ollama import Ollama

from .base import BaseLLM


class OllamaLLM(BaseLLM):

    def __init__(self):

        self.client = Ollama(
            model="qwen2.5:3b",
            request_timeout=120
        )

    def generate(self, prompt: str):

        response = self.client.complete(
            prompt
        )

        return response.text