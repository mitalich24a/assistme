from app.tools.base_tool import BaseTool


class GenerateTasksTool(BaseTool):

    @property
    def name(self):
        return "generate_tasks"

    @property
    def description(self):
        return "Generate engineering tasks from a design document."

    @property
    def input_schema(self):

        return {
            "type": "object",
            "properties": {
                "design_text": {
                    "type": "string"
                }
            },
            "required": [
                "design_text"
            ]
        }

    async def execute(
        self,
        arguments: dict,
    ):

        return {
            "message": "Tool executed successfully."
        }