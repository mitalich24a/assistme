from pydantic import BaseModel


class ReadFileRequest(BaseModel):
    path: str