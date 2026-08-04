from app.tools.tool_registry import ToolRegistry


class ToolExecutor:

    def __init__(
        self,
        registry: ToolRegistry,
    ):

        self._registry = registry

    async def execute(
        self,
        name: str,
        arguments: dict,
    ):

        tool = self._registry.get(
            name,
        )

        return await tool.execute(
            arguments,
        )