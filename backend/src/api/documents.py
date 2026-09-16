from typing import Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import Response
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.models import User
from src.services.auth_service import get_optional_user
from src.schemas.documents import (
    DocumentDelete,
    DocumentList,
    DocumentOut,
    DocumentStatusUpdate,
)
from src.services.document_service import DocumentService
from src.services.storage import get_storage

router = APIRouter()


@router.post("", response_model=DocumentOut, status_code=201)
async def upload_document(
    file: UploadFile = File(...),
    journey_id: int = Form(...),
    step_id: Optional[int] = Form(None),
    requirement: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Upload a file and attach it to a journey (optionally a step + requirement)."""
    content = await file.read()
    return DocumentService.upload(
        db,
        file=file,
        content=content,
        user_id=user.id if user else None,
        journey_id=journey_id,
        step_id=step_id,
        requirement=requirement,
    )


@router.get("", response_model=DocumentList)
def list_documents(
    journey_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    """List documents, optionally filtered by journey."""
    docs = DocumentService.list(db, journey_id=journey_id)
    return {"documents": docs, "total": len(docs)}


@router.get("/{document_id}/download")
def download_document(document_id: int, db: Session = Depends(get_db)):
    """Stream the stored file back to the client."""
    doc = DocumentService.get_or_404(db, document_id)
    data = DocumentService.read_content(document_id, doc)
    return Response(
        content=data,
        media_type=doc.file_type,
        headers={
            "Content-Disposition": f'attachment; filename="{doc.filename}"'
        },
    )


@router.get("/{document_id}", response_model=DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    """Get a single document's metadata."""
    return DocumentService.get_or_404(db, document_id)


@router.patch("/{document_id}/status", response_model=DocumentOut)
def update_document_status(
    document_id: int,
    data: DocumentStatusUpdate,
    db: Session = Depends(get_db),
):
    """Update a document's verification status."""
    return DocumentService.update_status(db, document_id, data.status)


@router.delete("/{document_id}", response_model=DocumentDelete)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    """Delete a document and its stored file."""
    deleted_id = DocumentService.delete(db, document_id)
    return {"deleted": True, "id": deleted_id}