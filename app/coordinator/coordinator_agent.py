from app.execution.workflow_context import WorkflowContext
from app.registry.agent_registry import AgentRegistry
from app.schemas.agent_result import AgentResult


class CoordinatorAgent:
    """
    Delegates workflow execution to the appropriate agent.
    """

    def __init__(
        self,
        registry: AgentRegistry,
    ) -> None:

        self._registry = registry

    async def execute(
        self,
        capability: str,
        context: WorkflowContext,
        **kwargs,
    ) -> AgentResult:

        agent = self._registry.get(
            capability,
        )

        if agent is None:
            raise ValueError(
                f"No agent registered for capability: {capability}"
            )

        return await agent.run(
            context=context,
            **kwargs,
        )