import shutil
import subprocess
import time

import httpx


class OllamaManager:

    @staticmethod
    def is_installed() -> bool:
        return shutil.which("ollama") is not None

    @staticmethod
    def install() -> None:
        raise NotImplementedError(
            "Automatic Ollama installation is not implemented yet."
        )

    @staticmethod
    def is_running() -> bool:
        try:
            response = httpx.get(
                "http://127.0.0.1:11434/api/tags",
                timeout=2.0,
            )

            return response.status_code == 200

        except Exception:
            return False

    @staticmethod
    def start() -> None:

        if OllamaManager.is_running():
            return

        print("Starting Ollama...")

        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        #
        # Wait until Ollama is ready.
        #
        for _ in range(30):

            if OllamaManager.is_running():
                print("Ollama is ready.")
                return

            time.sleep(1)

        raise RuntimeError(
            "Timed out waiting for Ollama to start."
        )

    @staticmethod
    def has_model(
        model: str,
    ) -> bool:

        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True,
        )

        return model in result.stdout

    @staticmethod
    def pull_model(
        model: str,
    ) -> None:

        subprocess.run(
            ["ollama", "pull", model],
            check=True,
        )