from app.core.interfaces.base_agent import BaseAgent
from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.execution.workflow_context import WorkflowContext
from app.schemas.agent_result import AgentResult


class PlannerAgent(BaseAgent):
    """
    Responsible for converting a high-level goal into
    an executable plan.
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
        return "Generates execution plans using an LLM."
    
    @property
    def capabilities(self) -> list[str]:
        return [
            "planning",
            "task-decomposition",
        ]

    async def run(
        self,
        context: WorkflowContext,
        **kwargs,
    ) -> AgentResult:

        prompt = kwargs.get("prompt", "")

        response = await self._llm_provider.generate(prompt)

        return AgentResult(
            success=True,
            data={
                "plan": response
            },
            message="Planning completed successfully."
        )