from app.constants.capabilities import Capabilities
from app.core.interfaces.base_agent import BaseAgent
from app.execution.workflow_context import WorkflowContext
from app.schemas.agent_result import AgentResult
from app.services.mcp_service import McpService


class McpAgent(BaseAgent):
    """
    Agent responsible for interacting with MCP servers.
    """

    def __init__(self) -> None:
        self._service = McpService()

    @property
    def name(self) -> str:
        return "McpAgent"

    @property
    def description(self) -> str:
        return "Executes MCP tools."

    @property
    def capabilities(self) -> list[str]:
        return [Capabilities.MCP]

    async def run(
        self,
        context: WorkflowContext,
        **kwargs,
    ) -> AgentResult:

        path = kwargs.get("path")

        if path:
            result = await self._service.read_file(path)

            return AgentResult(
                success=True,
                data={
                    "content": result,
                },
                message="File read successfully.",
            )

        result = await self._service.list_tools()

        return AgentResult(
            success=True,
            data={
                "mcp": result,
            },
            message="MCP tools listed successfully.",
        )