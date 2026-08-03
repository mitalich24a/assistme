from pydantic import BaseModel


class PublishedIssue(BaseModel):
    title: str

    issue_number: int

    issue_url: str