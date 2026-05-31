from fastapi import APIRouter
from api.models.model import QueryRequest
from rag.service import RAGService

router = APIRouter()

@router.post("/query")
def query(request: QueryRequest):
    answer = RAGService().query(request.question)
    return {"answer": answer}
