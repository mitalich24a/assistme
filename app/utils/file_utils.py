import shutil
from pathlib import Path

from fastapi import UploadFile


class FileUtils:

    UPLOAD_DIR = Path("uploads")

    @classmethod
    def save(cls, file: UploadFile) -> str:

        cls.UPLOAD_DIR.mkdir(exist_ok=True)

        destination = cls.UPLOAD_DIR / file.filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return str(destination)