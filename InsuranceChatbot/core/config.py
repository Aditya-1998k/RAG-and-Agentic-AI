from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    VECTOR_DB_PATH: str = "./chroma_db"
    CHROMA_COLLECTION: str = "documents"
    TOP_K: int = 5

    class Config:
        env_file = ".env"


settings = Settings()