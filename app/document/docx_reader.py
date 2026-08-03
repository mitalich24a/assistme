from docx import Document


class DocxReader:

    @staticmethod
    def read(file_path: str) -> str:

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)