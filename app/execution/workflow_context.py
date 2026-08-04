from dataclasses import dataclass, field

from app.execution.workflow_memory import WorkflowMemory


@dataclass
class WorkflowContext:
    """
    Shared state for a workflow execution.
    """

    workflow_id: str

    input_data: dict = field(
        default_factory=dict,
    )

    output_data: dict = field(
        default_factory=dict,
    )

    metadata: dict = field(
        default_factory=dict,
    )

    memory: WorkflowMemory = field(
        default_factory=WorkflowMemory,
    )