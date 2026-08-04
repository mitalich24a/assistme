from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.prompts.review_prompt import REVIEW_SYSTEM_PROMPT
from app.schemas.planning_result import PlanningResult
from app.utils.parsers.json_parser import JsonParser


class ReviewAgent:
    """
    Reviews and validates the generated sprint plan.
    """

    def __init__(
        self,
        llm_provider: BaseLLMProvider,
    ) -> None:

        self._llm_provider = llm_provider

    async def run(
        self,
        planning: PlanningResult,
    ) -> PlanningResult:

        response = await self._llm_provider.generate(
            system_prompt=REVIEW_SYSTEM_PROMPT,
            user_prompt=planning.model_dump_json(indent=2),
        )

        return JsonParser.parse(
            response=response,
            schema=PlanningResult,
        )