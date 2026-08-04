from app.checkpoint.checkpoint import Checkpoint
from app.checkpoint.checkpoint_manager import CheckpointManager
from app.coordinator.coordinator_agent import CoordinatorAgent
from app.execution.workflow_context import WorkflowContext
from app.execution.workflow_definition import WorkflowDefinition
from app.schemas.agent_result import AgentResult


class RuntimeExecutor:
    """
    Executes a workflow step by step with checkpoint support.
    """

    def __init__(
        self,
        coordinator: CoordinatorAgent,
    ) -> None:

        self._coordinator = coordinator
        self._checkpoint_manager = CheckpointManager()

    async def execute(
        self,
        workflow: WorkflowDefinition,
        context: WorkflowContext,
    ) -> list[AgentResult]:

        checkpoint = self._checkpoint_manager.load(
            context.workflow_id,
        )

        if checkpoint is None:

            checkpoint = Checkpoint(
                workflow_id=context.workflow_id,
            )

        results: list[AgentResult] = []

        #
        # Resume from last unfinished step
        #
        for index, step in enumerate(workflow.steps):

            if index < checkpoint.current_step:
                continue

            result = await self._coordinator.execute(
                context=context,
                capability=step.capability,
                **step.input_data,
            )

            results.append(result)
            context.output_data.update(
                result.data
            )

            checkpoint.current_step = index + 1

            checkpoint.completed_steps.append(
                step.name,
            )

            self._checkpoint_manager.save(
                checkpoint,
            )

        checkpoint.status = "COMPLETED"

        self._checkpoint_manager.save(
            checkpoint,
        )

        return results