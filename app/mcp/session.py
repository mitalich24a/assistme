class McpSession:
    """
    Holds a connection to an MCP server.

    This will later wrap the official MCP ClientSession.
    """

    def __init__(self) -> None:
        self.connected = False

    async def connect(self) -> None:
        self.connected = True

    async def disconnect(self) -> None:
        self.connected = False