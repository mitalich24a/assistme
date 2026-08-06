from app.mcp.client.session_manager import SessionManager
from app.mcp.config import SERVERS


class McpClient:

    def __init__(self):

        self.sessions = SessionManager()

        for server in SERVERS:

            self.sessions.register(
                name=server.name,
                server=server,
            )