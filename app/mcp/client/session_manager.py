from app.mcp.client.session import Session


class SessionManager:

    def __init__(self):

        self._sessions = {}

    def register(
        self,
        name: str,
        server,
    ):

        self._sessions[name] = Session(
            name=name,
            server=server,
        )

    def get(
        self,
        name: str,
    ) -> Session:

        return self._sessions[name]

    def all(
        self,
    ) -> list[Session]:

        return list(
            self._sessions.values()
        )