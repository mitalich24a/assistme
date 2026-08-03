from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowContext:
    workflow_id: str
    workflow_name: str

    input_data: dict[str, Any] = field(default_factory=dict)
    output_data: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)