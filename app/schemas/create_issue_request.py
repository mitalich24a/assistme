from pydantic import BaseModel


class CreateIssueRequest(BaseModel):
    title: str

    body: str