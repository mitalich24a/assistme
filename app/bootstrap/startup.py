import uvicorn

from app.bootstrap.mcp_server_starter import McpServerStarter


class Startup:

    @staticmethod
    def run() -> None:

        McpServerStarter.start()

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )