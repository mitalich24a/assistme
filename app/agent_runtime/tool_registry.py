from app.services.mcp_service import McpService


class ToolRegistry:

    def __init__(self):

        self._mcp = McpService()

    def definitions(self):

        return [
            {
                "type": "function",
                "function": {
                    "name": "read_text_file",
                    "description": "Read a text file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "path"
                        ],
                    },
                },
            }
        ]

    async def execute(
        self,
        name: str,
        arguments: dict,
    ):

        if name == "read_text_file":

            return await self._mcp.read_file(
                arguments["path"]
            )

        raise ValueError(name)