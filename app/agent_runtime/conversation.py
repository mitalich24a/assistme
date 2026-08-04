from pydantic import BaseModel, Field


class Conversation(BaseModel):
    """
    Maintains the conversation between
    the user, assistant and tools.
    """

    messages: list[dict] = Field(default_factory=list)

    def user(
        self,
        content: str,
    ):

        self.messages.append(
            {
                "role": "user",
                "content": content,
            }
        )

    def assistant(
        self,
        content: str,
    ):

        self.messages.append(
            {
                "role": "assistant",
                "content": content,
            }
        )

    def tool(
        self,
        tool_name: str,
        content: str,
    ):

        self.messages.append(
            {
                "role": "tool",
                "name": tool_name,
                "content": content,
            }
        )