from app.config.settings import settings
from app.core.interfaces.base_publishing_service import (
    BasePublishingService,
)
from app.publishing.github_publishing_service import (
    GitHubPublishingService,
)


class PublishingService:

    @staticmethod
    def create() -> BasePublishingService:

        if settings.publish_provider == "github":
            return GitHubPublishingService()

        raise ValueError(
            f"Unsupported publishing provider: {settings.publish_provider}"
        )