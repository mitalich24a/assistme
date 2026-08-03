from pathlib import Path

from app.document.document_type import DocumentType
from app.document.docx_reader import DocxReader
from app.document.markdown_reader import MarkdownReader
from app.document.pdf_reader import PdfReader
from app.document.text_reader import TextReader


class DocumentService:

    @staticmethod
    def extract(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == DocumentType.PDF:
            return PdfReader.read(file_path)

        if extension == DocumentType.DOCX:
            return DocxReader.read(file_path)

        if extension == DocumentType.MARKDOWN:
            return MarkdownReader.read(file_path)

        if extension == DocumentType.TEXT:
            return TextReader.read(file_path)

        raise ValueError(
            f"Unsupported document type: {extension}"
        )