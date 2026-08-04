from app.tools.base_tool import BaseTool


class Registry:

    def __init__(self):

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        self._tools[tool.name] = tool

    def get(
        self,
        name: str,
    ) -> BaseTool:

        return self._tools[name]

    def has(
        self,
        name: str,
    ) -> bool:

        return name in self._tools

    def list(
        self,
    ) -> list:

        tools = []

        for tool in self._tools.values():

            tools.append(
                {
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.input_schema,
                    },
                }
            )

        return tools