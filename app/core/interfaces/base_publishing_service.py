from abc import ABC, abstractmethod

from app.schemas.planning_result import PlanningResult
from app.schemas.publish_result import PublishResult


class BasePublishingService(ABC):
    """
    Base contract for publishing sprint plans.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def publish(
        self,
        planning: PlanningResult,
    ) -> PublishResult:
        raise NotImplementedError