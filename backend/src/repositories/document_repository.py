from sqlalchemy.orm import Session

from src.models.models import Document


class DocumentRepository:
    """All SQLAlchemy queries for documents live here."""

    @staticmethod
    def create(
        db: Session,
        *,
        user_id: int | None,
        journey_id: int,
        step_id: int | None,
        requirement: str | None,
        filename: str,
        file_type: str,
        file_size: int,
        storage_path: str,
        status: str = "UPLOADED",
    ) -> Document:
        doc = Document(
            user_id=user_id,
            journey_id=journey_id,
            step_id=step_id,
            requirement=requirement,
            filename=filename,
            file_type=file_type,
            file_size=file_size,
            storage_path=storage_path,
            status=status,
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc

    @staticmethod
    def get(db: Session, document_id: int) -> Document | None:
        return db.query(Document).filter(Document.id == document_id).first()

    @staticmethod
    def list_all(db: Session) -> list[Document]:
        return (
            db.query(Document)
            .order_by(Document.created_at.desc())
            .all()
        )

    @staticmethod
    def list_by_journey(db: Session, journey_id: int) -> list[Document]:
        return (
            db.query(Document)
            .filter(Document.journey_id == journey_id)
            .order_by(Document.created_at.desc())
            .all()
        )

    @staticmethod
    def update_status(db: Session, document_id: int, status: str) -> Document | None:
        doc = DocumentRepository.get(db, document_id)
        if not doc:
            return None
        doc.status = status
        db.commit()
        db.refresh(doc)
        return doc

    @staticmethod
    def delete(db: Session, document_id: int) -> bool:
        doc = DocumentRepository.get(db, document_id)
        if not doc:
            return False
        db.delete(doc)
        db.commit()
        return True