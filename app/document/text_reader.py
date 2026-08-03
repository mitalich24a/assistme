from pathlib import Path


class TextReader:

    @staticmethod
    def read(file_path: str) -> str:
        return Path(file_path).read_text(encoding="utf-8")