from app.core.interfaces.base_tool import BaseTool


class ToolRegistry:
    """
    Registry for all available tools.
    """

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        self._tools[tool.tool_name] = tool

    def get(
        self,
        name: str,
    ) -> BaseTool:
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' is not registered.")

        return self._tools[name]

    def all(self) -> list[BaseTool]:
        return list(self._tools.values())