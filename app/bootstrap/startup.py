import uvicorn

from app.main import app


class Startup:

    @staticmethod
    def run() -> None:

        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            reload=True,
        )