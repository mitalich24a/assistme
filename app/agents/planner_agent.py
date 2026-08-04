from app.agents.workers.dependency_agent import DependencyAgent
from app.agents.workers.review_agent import ReviewAgent
from app.agents.workers.story_point_agent import StoryPointAgent
from app.agents.workers.task_generator_agent import TaskGeneratorAgent
from app.constants.capabilities import Capabilities
from app.core.interfaces.base_agent import BaseAgent
from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.execution.retry_executor import RetryExecutor
from app.execution.workflow_context import WorkflowContext
from app.schemas.agent_result import AgentResult


class PlannerAgent(BaseAgent):
    """
    Coordinates sprint planning using specialized worker agents.
    """

    def __init__(
        self,
        llm_provider: BaseLLMProvider,
    ) -> None:

        self._retry = RetryExecutor()

        self._task_generator = TaskGeneratorAgent(
            llm_provider=llm_provider,
        )

        self._story_point_agent = StoryPointAgent(
            llm_provider=llm_provider,
        )

        self._dependency_agent = DependencyAgent(
            llm_provider=llm_provider,
        )

        self._review_agent = ReviewAgent(
            llm_provider=llm_provider,
        )

    @property
    def name(self) -> str:
        return "PlannerAgent"

    @property
    def description(self) -> str:
        return "Coordinates sprint planning using specialized worker agents."

    @property
    def capabilities(self) -> list[str]:
        return [
            Capabilities.PLANNING,
        ]

    async def run(
        self,
        context: WorkflowContext,
        **kwargs,
    ) -> AgentResult:

        design_text = context.input_data["design_text"]

        planning = await self._retry.execute(
            self._task_generator.run,
            design_text,
        )

        planning = await self._retry.execute(
            self._story_point_agent.run,
            planning,
        )

        planning = await self._retry.execute(
            self._dependency_agent.run,
            planning,
        )

        planning = await self._retry.execute(
            self._review_agent.run,
            planning,
        )

        #
        # Save into workflow memory
        #
        context.memory.set(
            "planning",
            planning,
        )

        return AgentResult(
            success=True,
            data={
                "planning": planning,
            },
            message="Planning completed successfully.",
        )