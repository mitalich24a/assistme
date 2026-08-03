from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowStep:
    """
    Represents a single executable step in a workflow.
    """

    name: str

    capability: str

    input_data: dict[str, Any] = field(default_factory=dict)