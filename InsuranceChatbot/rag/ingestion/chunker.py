from llama_index.core.node_parser import SentenceSplitter


class Chunker:
    """Utility class for chunking documents into smaller pieces."""

    @staticmethod
    def get():
        return SentenceSplitter(
            chunk_size=1024,
            chunk_overlap=100
        )
