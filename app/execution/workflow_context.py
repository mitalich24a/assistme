from dataclasses import dataclass, field
from typing import Any

from app.execution.workflow_status import WorkflowStatus


@dataclass
class WorkflowContext:

    workflow_id: str

    workflow_name: str

    status: WorkflowStatus = WorkflowStatus.PENDING

    input_data: dict[str, Any] = field(default_factory=dict)

    output_data: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)