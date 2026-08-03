import fitz


class PdfReader:

    @staticmethod
    def read(file_path: str) -> str:

        document = fitz.open(file_path)

        pages = []

        for page in document:
            pages.append(page.get_text())

        document.close()

        return "\n".join(pages)