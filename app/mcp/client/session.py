from app.mcp.mcp_session import McpSession


class Session:

    def __init__(
        self,
        name: str,
        server,
    ):

        self._name = name
        self._server = server

    @property
    def name(self):

        return self._name

    async def __aenter__(self):

        self._session = McpSession(
            self._server,
        )

        return await self._session.__aenter__()

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ):

        return await self._session.__aexit__(
            exc_type,
            exc,
            tb,
        )