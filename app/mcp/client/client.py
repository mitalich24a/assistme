from app.mcp.client.session_manager import SessionManager
from app.mcp.config import SERVERS


class McpClient:

    def __init__(self):

        self._manager = SessionManager()

        for name, server in SERVERS.items():

            self._manager.register(
                name,
                server,
            )

    @property
    def sessions(
        self,
    ) -> SessionManager:

        return self._manager