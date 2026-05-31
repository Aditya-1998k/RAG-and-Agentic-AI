from fastapi import FastAPI
from api.routes.ingest import router as ingest_router
from api.routes.query import router as query_router

app = FastAPI()

app.include_router(ingest_router)
app.include_router(query_router)
