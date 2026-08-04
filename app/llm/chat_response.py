from pydantic import BaseModel, Field

from app.llm.tool_call import ToolCall


class ChatResponse(BaseModel):
    """
    Generic response returned by any LLM provider.
    """

    content: str = ""

    tool_calls: list[ToolCall] = Field(
        default_factory=list,
    )

    @property
    def has_tool_calls(self) -> bool:
        return len(self.tool_calls) > 0