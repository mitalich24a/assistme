from fastmcp import FastMCP


def register_create_sprint_plan(
    mcp,
):

    @mcp.tool()
    async def create_sprint_plan(
        requirements: str,
    ) -> dict:
        """
        Analyze software requirements and generate
        an engineering sprint plan.
        """

        return {
            "goal": (
                "Break requirements into engineering tasks."
            ),
            "tasks": [
                {
                    "title": "Implement AI Agent Runtime",
                    "description": (
                        "Build the reasoning loop, "
                        "conversation handling and tool execution."
                    ),
                    "priority": "High",
                },
                {
                    "title": "Implement MCP Client",
                    "description": (
                        "Connect to external MCP servers and "
                        "discover tools dynamically."
                    ),
                    "priority": "High",
                },
                {
                    "title": "Implement MCP Server",
                    "description": (
                        "Expose local tools through FastMCP."
                    ),
                    "priority": "High",
                },
            ],
        }