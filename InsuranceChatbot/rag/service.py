from rag.llms.gemini import GeminiLLM
from rag.retrival.retrieval import Retriever
from rag.retrival.reranker import Reranker

class RAGService:

    def __init__(self):
        self.retriever = Retriever()
        self.reranker = Reranker()
        self.llm = GeminiLLM().get_client()

        def query(self, question):
            nodes = self.retriever.get().retrieve(question)
            nodes = self.reranker.rerank(question, nodes)
            context = "\n".join(
                [
                    node.text
                    for node in nodes
                ]
            )

            prompt = f"""
            Context: {context}
            Question: {question}
            Answer only from context.
            """
            response = self.llm.complete(prompt)

            return response.text