import json
from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class JsonParser:
    """
    Parses LLM JSON into a Pydantic model.
    """

    @staticmethod
    def parse(
        response: str,
        schema: Type[T],
    ) -> T:

        response = response.strip()

        if response.startswith("```json"):
            response = response[7:]

        if response.endswith("```"):
            response = response[:-3]

        response = response.strip()

        data = json.loads(response)

        return schema.model_validate(data)