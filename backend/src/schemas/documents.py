from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class DocumentStatusUpdate(BaseModel):
    status: str  # UPLOADED | IN_REVIEW | VERIFIED | REJECTED


class DocumentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    journey_id: Optional[int] = None
    step_id: Optional[int] = None
    requirement: Optional[str] = None
    filename: str
    file_type: str
    file_size: int
    storage_path: str
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DocumentList(BaseModel):
    documents: List[DocumentOut]
    total: int


class DocumentDelete(BaseModel):
    deleted: bool
    id: int