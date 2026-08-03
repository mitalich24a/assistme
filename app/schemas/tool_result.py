from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolResult:
    success: bool

    output: dict[str, Any] = field(default_factory=dict)

    message: str = ""