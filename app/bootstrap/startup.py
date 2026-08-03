import uvicorn


class Startup:

    @staticmethod
    def run() -> None:

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )