from fastapi import APIRouter
from rag.ingestion.pipeline import IngestionPipeline

router = APIRouter()

@router.post("/ingest")
def ingest():
    IngestionPipeline().run("./data")

    return {"status": "success"}