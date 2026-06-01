from rag.llms.factory import LLMFactory
from rag.retrival.retrieval import Retriever
from rag.retrival.reranker import Reranker


class RAGService:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.llm = LLMFactory.create_llm()

    def query(self, question):

        nodes = (
            self.retriever
            .get()
            .retrieve(question)
        )

        nodes = (
            self.reranker
            .rerank(question, nodes)
        )

        context = "\n".join(
            node.text
            for node in nodes
        )

        prompt = f"""
        Context:
        {context}

        Question:
        {question}

        Answer only from the provided context.
        """

        return self.llm.generate(prompt)