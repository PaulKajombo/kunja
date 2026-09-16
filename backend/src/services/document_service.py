import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.config import settings
from src.models.models import Document
from src.repositories.document_repository import DocumentRepository
from src.services.storage import get_storage

VALID_STATUSES = {"MISSING", "UPLOADED", "IN_REVIEW", "VERIFIED", "REJECTED"}
ALLOWED_EXTENSIONS = {
    e.strip().lower() for e in settings.ALLOWED_UPLOAD_EXTENSIONS.split(",") if e.strip()
}


class DocumentService:
    @staticmethod
    def _validate(filename: str, size: int) -> str:
        ext = Path(filename).suffix.lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type {ext!r}. Allowed: {sorted(ALLOWED_EXTENSIONS)}",
            )
        max_bytes = settings.MAX_UPLOAD_MB * 1024 * 1024
        if size > max_bytes:
            raise HTTPException(
                status_code=400,
                detail=f"File exceeds the {settings.MAX_UPLOAD_MB} MB limit",
            )
        return ext

    @staticmethod
    def upload(
        db: Session,
        *,
        file: UploadFile,
        content: bytes,
        user_id: int | None,
        journey_id: int,
        step_id: int | None,
        requirement: str | None = None,
    ) -> Document:
        filename = file.filename or "unnamed"
        ext = DocumentService._validate(filename, len(content))

        key = f"journey_{journey_id}/{uuid.uuid4().hex}{ext}"
        get_storage().save(key, content, file.content_type or "application/octet-stream")

        return DocumentRepository.create(
            db,
            user_id=user_id,
            journey_id=journey_id,
            step_id=step_id,
            requirement=requirement,
            filename=filename,
            file_type=file.content_type or "application/octet-stream",
            file_size=len(content),
            storage_path=key,
        )

    @staticmethod
    def list(db: Session, journey_id: int | None = None) -> list[Document]:
        if journey_id is not None:
            return DocumentRepository.list_by_journey(db, journey_id)
        return DocumentRepository.list_all(db)

    @staticmethod
    def get_or_404(db: Session, document_id: int) -> Document:
        doc = DocumentRepository.get(db, document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    @staticmethod
    def update_status(db: Session, document_id: int, status: str) -> Document:
        if status not in VALID_STATUSES:
            raise HTTPException(
                status_code=400,
                detail=f"status must be one of: {sorted(VALID_STATUSES)}",
            )
        doc = DocumentRepository.update_status(db, document_id, status)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc

    @staticmethod
    def delete(db: Session, document_id: int) -> int:
        doc = DocumentRepository.get(db, document_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        get_storage().delete(doc.storage_path)
        DocumentRepository.delete(db, document_id)
        return doc.id

    @staticmethod
    def read_content(document_id: int, doc: Document) -> bytes:
        try:
            return get_storage().open(doc.storage_path)
        except FileNotFoundError:
            raise HTTPException(
                status_code=404, detail="Stored file is missing from the storage backend"
            ) from None