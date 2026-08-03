import httpx

from app.config.settings import settings
from app.core.interfaces.base_github_client import BaseGitHubClient
from app.schemas.create_issue_request import CreateIssueRequest
from app.schemas.published_issue import PublishedIssue


class GitHubRestClient(BaseGitHubClient):

    @property
    def provider_name(self) -> str:
        return "github-rest"

    async def create_issue(
        self,
        issue: CreateIssueRequest,
    ) -> PublishedIssue:

        if not settings.github_token:
            raise ValueError(
                "GITHUB_TOKEN is not configured."
            )

        if not settings.github_owner:
            raise ValueError(
                "GITHUB_OWNER is not configured."
            )

        if not settings.github_repo:
            raise ValueError(
                "GITHUB_REPO is not configured."
            )

        url = (
            f"https://api.github.com/repos/"
            f"{settings.github_owner}/"
            f"{settings.github_repo}/issues"
        )

        headers = {
            "Authorization": f"Bearer {settings.github_token}",
            "Accept": "application/vnd.github+json",
        }

        payload = {
            "title": issue.title,
            "body": issue.body,
        }

        async with httpx.AsyncClient() as client:

            response = await client.post(
                url,
                headers=headers,
                json=payload,
            )

        response.raise_for_status()

        data = response.json()

        return PublishedIssue(
            title=data["title"],
            issue_number=data["number"],
            issue_url=data["html_url"],
        )