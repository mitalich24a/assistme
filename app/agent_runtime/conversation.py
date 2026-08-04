from pydantic import BaseModel, Field


class Conversation(BaseModel):

    messages: list[dict] = Field(default_factory=list)

    def user(self, message: str):

        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def assistant(self, message: str):

        self.messages.append(
            {
                "role": "assistant",
                "content": message,
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