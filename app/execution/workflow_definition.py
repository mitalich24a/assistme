from dataclasses import dataclass, field

from app.execution.workflow_step import WorkflowStep


@dataclass
class WorkflowDefinition:
    """
    Defines the execution plan for a workflow.
    """

    name: str

    steps: list[WorkflowStep] = field(default_factory=list)