import subprocess
import sys
import time

from app.config.settings import settings


class McpServerStarter:

    @staticmethod
    def start() -> None:

        if settings.mcp_transport == "stdio":

            print("Starting MCP STDIO Server...")

            subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "app.mcp.server.stdio_server",
                ]
            )

        elif settings.mcp_transport == "http":

            print("Starting MCP HTTP Server...")

            subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "app.mcp.server.http_server",
                ]
            )

        else:

            raise ValueError(
                f"Unsupported transport: {settings.mcp_transport}"
            )

        #
        # TODO:
        # Replace with readiness check.
        #
        time.sleep(3)