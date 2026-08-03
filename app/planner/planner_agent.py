from app.constants.capabilities import Capabilities
from app.core.interfaces.base_agent import BaseAgent
from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.execution.workflow_context import WorkflowContext
from app.prompts.planner_prompt import PLANNER_SYSTEM_PROMPT
from app.schemas.agent_result import AgentResult

from app.schemas.planning_result import PlanningResult
from app.utils.parsers.json_parser import JsonParser


class PlannerAgent(BaseAgent):
    """
    Generates an implementation plan from a design document.
    """

    def __init__(
        self,
        llm_provider: BaseLLMProvider,
    ) -> None:
        self._llm_provider = llm_provider

    @property
    def name(self) -> str:
        return "PlannerAgent"

    @property
    def description(self) -> str:
        return "Generates engineering implementation plans."

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

        response = await self._llm_provider.generate(
            system_prompt=PLANNER_SYSTEM_PROMPT,
            user_prompt=design_text,
        )

        planning = JsonParser.parse(
            response=response,
            schema=PlanningResult,
        )

        return AgentResult(
            success=True,
            data={
                "planning": planning.model_dump(),
            },
            message="Planning completed successfully.",
        )