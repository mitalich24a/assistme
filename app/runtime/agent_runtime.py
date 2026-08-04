import json
import time

from app.llm.ollama_provider import OllamaProvider
from app.services.mcp_service import McpService
from app.tools.hybrid_executor import HybridExecutor
from app.tools.registry import Registry


class AgentRuntime:

    def __init__(
        self,
        registry: Registry,
    ):

        self._provider = OllamaProvider()
        self._registry = registry
        self._executor = HybridExecutor(
            registry,
        )
        self._mcp = McpService()

    async def run(
        self,
        prompt: str,
    ) -> str:

        print("\n==============================")
        print("AGENT START")
        print("==============================")

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        async with self._mcp.create_session() as session:

            print("\nLoading Local Tools...")

            local_tools = self._registry.list()

            print(
                f"Local Tools: {len(local_tools)}"
            )

            print("\nLoading MCP Tools...")

            start = time.time()

            mcp_tools = await session.list_ollama_tools()

            print(
                f"MCP Tools: {len(mcp_tools)}"
            )

            print(
                f"MCP Tool Load Time: {time.time()-start:.2f}s"
            )

            #
            # TEMP
            # Disable MCP tools for debugging
            #
            tools = local_tools

            print(
                f"\nTotal Tools Sent To LLM: {len(tools)}"
            )

            iteration = 1

            while iteration <= 10:

                print("\n------------------------------")
                print(
                    f"Iteration {iteration}"
                )
                print("------------------------------")

                start = time.time()

                response = await self._provider.chat(
                    messages=messages,
                    tools=tools,
                )

                print(
                    f"LLM Time: {time.time()-start:.2f}s"
                )

                if not response.message.tool_calls:

                    print(
                        "\nNo Tool Calls."
                    )

                    print(
                        "FINAL RESPONSE:"
                    )

                    print(
                        response.message.content
                    )

                    return response.message.content

                print(
                    f"Tool Calls: {len(response.message.tool_calls)}"
                )

                for tc in response.message.tool_calls:

                    print(
                        f" -> {tc.function.name}"
                    )

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

                for tool_call in response.message.tool_calls:

                    print(
                        f"\nExecuting Tool: {tool_call.function.name}"
                    )

                    start = time.time()

                    result = await self._executor.execute(
                        session=session,
                        tool_name=tool_call.function.name,
                        arguments=tool_call.function.arguments,
                    )

                    print(
                        f"Execution Time: {time.time()-start:.2f}s"
                    )

                    if isinstance(result, dict):

                        tool_output = json.dumps(
                            result,
                            indent=2,
                        )

                    else:

                        tool_output = ""

                        if (
                            hasattr(result, "content")
                            and result.content
                        ):
                            tool_output = (
                                result.content[0].text
                            )

                    messages.append(
                        {
                            "role": "tool",
                            "name": tool_call.function.name,
                            "content": tool_output,
                        }
                    )

                iteration += 1

        raise RuntimeError(
            "Maximum tool iterations exceeded."
        )