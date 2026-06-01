from core.config import settings
from .base import BaseLLM
from .gemini import GeminiLLM
from .ollama import OllamaLLM


class LLMFactory:
    """Factory for creating LLM instances based on configuration."""

    _llm_registry = {
        "gemini": GeminiLLM,
        "ollama": OllamaLLM,
    }

    @classmethod
    def create_llm(cls) -> BaseLLM:
        """
        Create an LLM instance based on the LLM_PROVIDER setting in config.

        Returns:
            BaseLLM: An instance of the configured LLM provider.

        Raises:
            ValueError: If the LLM_PROVIDER is not supported.
        """
        provider = settings.LLM_PROVIDER.lower()

        if provider not in cls._llm_registry:
            supported = ", ".join(cls._llm_registry.keys())
            raise ValueError(
                f"Unsupported LLM provider: {provider}. "
                f"Supported providers: {supported}"
            )

        llm_class = cls._llm_registry[provider]
        return llm_class()

    @classmethod
    def register_llm(cls, name: str, llm_class: type):
        """
        Register a new LLM provider.

        Args:
            name: The name of the LLM provider.
            llm_class: The LLM class to register.
        """
        cls._llm_registry[name] = llm_class
