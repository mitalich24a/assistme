from app.config.settings import settings
from app.core.interfaces.base_github_client import BaseGitHubClient
from app.github.github_rest_client import GitHubRestClient


class GitHubFactory:

    @staticmethod
    def create() -> BaseGitHubClient:

        if settings.publish_provider == "github":
            return GitHubRestClient()

        raise ValueError(
            f"Unsupported GitHub provider: {settings.publish_provider}"
        )