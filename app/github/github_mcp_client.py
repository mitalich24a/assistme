from app.core.interfaces.base_github_client import BaseGitHubClient
from app.schemas.create_issue_request import CreateIssueRequest
from app.schemas.published_issue import PublishedIssue


class GitHubMcpClient(BaseGitHubClient):
    """
    GitHub implementation using MCP.

    (Stub implementation. We'll wire the real MCP
    server next.)
    """

    @property
    def provider_name(self) -> str:
        return "github-mcp"

    async def create_issue(
        self,
        issue: CreateIssueRequest,
    ) -> PublishedIssue:

        raise NotImplementedError(
            "GitHub MCP integration is not implemented yet."
        )