import ollama

from app.config.settings import settings
from app.core.interfaces.base_llm_provider import BaseLLMProvider
from app.services.mcp_service import McpService


class OllamaProvider(BaseLLMProvider):

    def __init__(self):
        self._mcp = McpService()

    @property
    def provider_name(self) -> str:
        return "ollama"

    #
    # Used by Workflow Engine
    #
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

        return await self.chat(messages)

    #
    # Used by Agent Runtime
    #
    async def chat(
        self,
        messages: list[dict],
    ) -> str:

        async with self._mcp.create_session() as session:

            tools = await session.list_ollama_tools()

            while True:

                response = ollama.chat(
                    model=settings.ollama_model,
                    messages=messages,
                    tools=tools,
                )

                #
                # Final response
                #
                if not response.message.tool_calls:
                    return response.message.content

                #
                # Remember assistant tool call
                #
                messages.append(
                    {
                        "role": "assistant",
                        "content": response.message.content or "",
                        "tool_calls": [
                            {
                                "function": {
                                    "name": tc.function.name,
                                    "arguments": tc.function.arguments,
                                }
                            }
                            for tc in response.message.tool_calls
                        ],
                    }
                )

                #
                # Execute requested tools
                #
                for tool_call in response.message.tool_calls:

                    tool_result = await session.call_tool(
                        tool_call.function.name,
                        tool_call.function.arguments,
                    )

                    tool_output = ""

                    if tool_result.content:
                        tool_output = tool_result.content[0].text

                    messages.append(
                        {
                            "role": "tool",
                            "name": tool_call.function.name,
                            "content": tool_output,
                        }
                    )