from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass


class BaseEmbedding:

    async def embed(self, text: str) -> list[float]:
        pass