from app.execution.workflow_context import WorkflowContext
from app.registry.agent_registry import AgentRegistry
from app.schemas.agent_result import AgentResult


class CoordinatorAgent:
    """
    Coordinates workflow execution by delegating work
    to specialized agents.
    """

    def __init__(
        self,
        registry: AgentRegistry,
    ) -> None:
        self._registry = registry

    async def execute(
        self,
        context: WorkflowContext,
        capability: str,
        **kwargs,
    ) -> AgentResult:
        """
        Find the appropriate agent and execute it.
        """

        agent = self._registry.find(capability)

        return await agent.run(
            context=context,
            **kwargs,
        )