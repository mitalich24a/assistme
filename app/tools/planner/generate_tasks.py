from app.llm.factory import LLMFactory
from app.prompts.system_prompts import GENERATE_TASKS_PROMPT
from app.tools.base_tool import BaseTool


class GenerateTasksTool(BaseTool):

    def __init__(self):

        self._llm = LLMFactory.create()

    @property
    def name(self) -> str:
        return "generate_tasks"

    @property
    def description(self) -> str:
        return (
            "Generate engineering implementation tasks "
            "from a software design document."
        )

    @property
    def input_schema(self) -> dict:

        return {
            "type": "object",
            "properties": {
                "design_text": {
                    "type": "string",
                    "description": "Software design document."
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

        design_text = arguments["design_text"]

        response = await self._llm.generate(
            system_prompt=GENERATE_TASKS_PROMPT,
            user_prompt=design_text,
        )

        return {
            "tasks": response,
        }