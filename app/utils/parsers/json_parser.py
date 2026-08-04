import json
from typing import Type
from typing import TypeVar

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

        #
        # Remove markdown fences
        #
        response = (
            response.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        #
        # Extract JSON object
        #
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "No JSON object found in LLM response."
            )

        response = response[start : end + 1]

        try:
            data = json.loads(
                response,
                strict=False,
            )

        except json.JSONDecodeError:

            #
            # Common repair:
            # remove unescaped control characters
            #
            cleaned = "".join(
                ch
                for ch in response
                if ch >= " " or ch in "\n\r\t"
            )

            data = json.loads(
                cleaned,
                strict=False,
            )

        return schema.model_validate(data)