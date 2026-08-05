import json
from contextlib import AsyncExitStack

from app.llm.ollama_provider import OllamaProvider
from app.mcp.client.client import McpClient


class AgentRuntime:

    def __init__(self):

        self._llm = OllamaProvider()
        self._mcp = McpClient()

    async def run(
        self,
        prompt: str,
    ) -> str:

        print("\n" + "=" * 80)
        print("AGENT START")
        print("=" * 80)

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        async with AsyncExitStack() as stack:

            sessions = []
            all_tools = []

            #
            # Connect to every MCP server
            #
            for session in self._mcp.sessions.all():

                print(f"\nConnecting to MCP Server: {session.name}")

                mcp_session = await stack.enter_async_context(
                    session,
                )

                sessions.append(
                    (
                        session.name,
                        mcp_session,
                    )
                )

                tools = await mcp_session.list_ollama_tools()

                print(f"Discovered {len(tools)} tools")

                for tool in tools:
                    print(
                        f"  - {tool['function']['name']}"
                    )

                all_tools.extend(
                    tools,
                )

            print("\n" + "=" * 80)
            print("TOTAL TOOLS SENT TO OLLAMA")
            print("=" * 80)

            for tool in all_tools:
                print(tool["function"]["name"])

            while True:

                response = await self._llm.chat(
                    messages=messages,
                    tools=all_tools,
                )

                print("\n" + "=" * 80)
                print("OLLAMA RESPONSE")
                print("=" * 80)

                print("Content:")
                print(response.message.content)

                print("\nTool Calls:")
                print(response.message.tool_calls)

                if not response.message.tool_calls:

                    print("\nFINAL RESPONSE")
                    print(response.message.content)

                    return response.message.content

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

                    tool_name = tool_call.function.name
                    arguments = tool_call.function.arguments

                    print("\n" + "=" * 80)
                    print("EXECUTING TOOL")
                    print("=" * 80)
                    print("Tool:", tool_name)
                    print("Arguments:", arguments)

                    result = None

                    #
                    # Find which MCP server owns this tool
                    #
                    for server_name, session in sessions:

                        tools = await session.list_tools()

                        tool_names = {
                            tool.name
                            for tool in tools.tools
                        }

                        if tool_name in tool_names:

                            print(
                                f"Executing on server: {server_name}"
                            )

                            result = await session.call_tool(
                                tool_name,
                                arguments,
                            )

                            break

                    if result is None:

                        raise RuntimeError(
                            f"Unknown tool: {tool_name}"
                        )

                    print("\nRaw Tool Result:")
                    print(result)

                    if result.content:

                        tool_output = "\n".join(
                            getattr(item, "text", str(item))
                            for item in result.content
                        )

                    else:

                        tool_output = json.dumps(
                            result.model_dump(),
                            indent=2,
                        )

                    print("\nTool Output:")
                    print(tool_output)

                    messages.append(
                        {
                            "role": "tool",
                            "name": tool_name,
                            "content": tool_output,
                        }
                    )