from app.constants.capabilities import Capabilities
from app.core.interfaces.base_agent import BaseAgent
from app.core.interfaces.base_publishing_service import (
    BasePublishingService,
)
from app.execution.workflow_context import WorkflowContext
from app.schemas.agent_result import AgentResult
from app.schemas.planning_result import PlanningResult


class PublisherAgent(BaseAgent):
    """
    Publishes a planning result.
    """

    def __init__(
        self,
        publishing_service: BasePublishingService,
    ) -> None:

        self._publishing_service = publishing_service

    @property
    def name(self) -> str:
        return "PublisherAgent"

    @property
    def description(self) -> str:
        return "Publishes planning results."

    @property
    def capabilities(self) -> list[str]:
        return [
            Capabilities.PUBLISHING,
        ]

    async def run(
        self,
        context: WorkflowContext,
        **kwargs,
    ) -> AgentResult:

        planning: PlanningResult = context.memory.get(
            "planning",
        )

        publish_result = await self._publishing_service.publish(
            planning,
        )

        context.memory.set(
            "publish_result",
            publish_result,
        )

        return AgentResult(
            success=True,
            data={
                "publish_result": publish_result,
            },
            message="Publishing completed successfully.",
        )