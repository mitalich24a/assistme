import json
from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class JsonParser:

    @staticmethod
    def parse(
        response: str,
        schema: Type[T],
    ) -> T:

        data = json.loads(response)

        return schema.model_validate(data)