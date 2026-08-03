from pydantic import BaseModel, Field

from app.schemas.published_issue import PublishedIssue


class PublishResult(BaseModel):

    repository: str

    issues: list[PublishedIssue] = Field(default_factory=list)