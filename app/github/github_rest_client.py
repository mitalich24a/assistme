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

        print("=" * 60)
        print("GitHubRestClient.create_issue()")
        print("=" * 60)

        if not settings.github_token:
            raise ValueError("GITHUB_TOKEN is not configured.")

        if not settings.github_owner:
            raise ValueError("GITHUB_OWNER is not configured.")

        if not settings.github_repo:
            raise ValueError("GITHUB_REPO is not configured.")

        url = (
            f"https://api.github.com/repos/"
            f"{settings.github_owner}/"
            f"{settings.github_repo}/issues"
        )

        print("URL:", url)
        print("Repository:", settings.github_owner + "/" + settings.github_repo)

        headers = {
            "Authorization": f"Bearer {settings.github_token}",
            "Accept": "application/vnd.github+json",
        }

        payload = {
            "title": issue.title,
            "body": issue.body,
        }

        print("Calling GitHub...")

        async with httpx.AsyncClient(timeout=30.0) as client:

            response = await client.post(
                url,
                headers=headers,
                json=payload,
            )

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        data = response.json()

        print("Issue created:", data["html_url"])

        return PublishedIssue(
            title=data["title"],
            issue_number=data["number"],
            issue_url=data["html_url"],
        )