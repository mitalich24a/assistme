from pathlib import Path

from app.tools.base_tool import BaseTool


class ReadFileTool(BaseTool):

    @property
    def name(self) -> str:
        return "read_file"

    @property
    def description(self) -> str:
        return "Read a text file from the local filesystem."

    @property
    def input_schema(self) -> dict:

        return {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Absolute or relative file path."
                }
            },
            "required": [
                "path"
            ]
        }

    async def execute(
        self,
        arguments: dict,
    ):

        path = Path(
            arguments["path"],
        )

        if not path.exists():

            return {
                "success": False,
                "error": f"{path} does not exist.",
            }

        return {
            "success": True,
            "path": str(path),
            "content": path.read_text(
                encoding="utf-8",
            ),
        }