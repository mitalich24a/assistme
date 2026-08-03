from app.coordinator.coordinator_agent import CoordinatorAgent
from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition
from app.schemas.agent_result import AgentResult


class RuntimeExecutor:
    """
    Executes a workflow definition step by step.
    """

    def __init__(
        self,
        coordinator: CoordinatorAgent,
    ) -> None:
        self._coordinator = coordinator

    async def execute(
        self,
        workflow: WorkflowDefinition,
        context: WorkflowContext,
    ) -> list[AgentResult]:

        results: list[AgentResult] = []

        for step in workflow.steps:

            result = await self._coordinator.execute(
                context=context,
                capability=step.capability,
                **step.input_data,
            )

            results.append(result)

        return results