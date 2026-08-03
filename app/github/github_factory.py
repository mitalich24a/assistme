from app.config.settings import settings
from app.core.interfaces.base_github_client import BaseGitHubClient
from app.github.github_rest_client import GitHubRestClient


class GitHubFactory:
    """
    Factory for GitHub client implementations.
    """

    @staticmethod
    def create() -> BaseGitHubClient:

        if settings.github_provider == "rest":
            return GitHubRestClient()

        if settings.github_provider == "mcp":
            from app.mcp.github.github_mcp_client import (
                GitHubMcpClient,
            )

            return GitHubMcpClient()

        raise ValueError(
            f"Unsupported GitHub provider: "
            f"{settings.github_provider}"
        )