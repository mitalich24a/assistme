from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.prompts.task_generator_prompt import TASK_GENERATOR_SYSTEM_PROMPT
from app.schemas.planning_result import PlanningResult
from app.utils.parsers.json_parser import JsonParser


class TaskGeneratorAgent:
    """
    Generates engineering implementation tasks
    from a software design document.
    """

    def __init__(
        self,
        llm_provider: BaseLLMProvider,
    ) -> None:

        self._llm_provider = llm_provider

    async def run(
        self,
        design_text: str,
    ) -> PlanningResult:

        response = await self._llm_provider.generate(
            system_prompt=TASK_GENERATOR_SYSTEM_PROMPT,
            user_prompt=design_text,
        )

        return JsonParser.parse(
            response=response,
            schema=PlanningResult,
        )