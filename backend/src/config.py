from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/kunja"
    SECRET_KEY: str = "kunja-dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"

    # Storage
    STORAGE_DRIVER: str = "local"  # local | s3 (future)
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_MB: int = 10
    ALLOWED_UPLOAD_EXTENSIONS: str = ".pdf,.docx,.xlsx,.png,.jpg,.jpeg,.gif,.webp"

    class Config:
        env_file = ".env"


settings = Settings()
