from enum import Enum

from pydantic import BaseModel


class DocumentType(str, Enum):
    TEXT = "text"
    PDF = "pdf"
    DOCX = "docx"
    MARKDOWN = "markdown"


class DocumentRequest(BaseModel):
    content: str
    document_type: DocumentType