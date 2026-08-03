from dataclasses import dataclass
from typing import Any


@dataclass
class McpToolResult:
    """
    Result returned from an MCP tool invocation.
    """

    success: bool

    data: Any = None

    message: str = ""