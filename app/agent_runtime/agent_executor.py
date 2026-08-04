import json

from app.agent_runtime.conversation import Conversation
from app.agent_runtime.tool_registry import ToolRegistry
from app.config.settings import settings
import ollama


class AgentExecutor:
    """
    Executes an AI conversation with MCP tool support.
    """

    def __init__(self):

        self._tools = ToolRegistry()

    async def chat(
        self,
        message: str,
    ) -> str:

        conversation = Conversation()

        conversation.user(message)

        #
        # Ask the LLM
        #
        response = ollama.chat(
            model=settings.ollama_model,
            messages=conversation.messages,
            tools=self._tools.definitions(),
        )

        #
        # Did the LLM request any tools?
        #
        tool_calls = response["message"].get("tool_calls", [])

        while tool_calls:

            for tool_call in tool_calls:

                tool_name = tool_call["function"]["name"]

                arguments = tool_call["function"]["arguments"]

                tool_result = await self._tools.execute(
                    tool_name,
                    arguments,
                )

                conversation.tool(
                    tool_name,
                    str(tool_result),
                )

            #
            # Ask the LLM again
            #
            response = ollama.chat(
                model=settings.ollama_model,
                messages=conversation.messages,
                tools=self._tools.definitions(),
            )

            tool_calls = response["message"].get(
                "tool_calls",
                [],
            )

        answer = response["message"]["content"]

        conversation.assistant(answer)

        return answer