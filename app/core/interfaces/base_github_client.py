from abc import ABC, abstractmethod

from app.schemas.create_issue_request import CreateIssueRequest
from app.schemas.published_issue import PublishedIssue


class BaseGitHubClient(ABC):

    @property
    @abstractmethod
    def provider_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def create_issue(
        self,
        issue: CreateIssueRequest,
    ) -> PublishedIssue:
        raise NotImplementedError