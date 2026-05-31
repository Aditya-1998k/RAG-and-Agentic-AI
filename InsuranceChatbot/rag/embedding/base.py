from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    """Abstract base class for embedding models."""

    @abstractmethod
    def get_model(self):
        """Get the embedding model instance."""
        pass
