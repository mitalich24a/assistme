import shutil
import subprocess


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
            subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                check=True,
            )
            return True

        except Exception:
            return False

    @staticmethod
    def start() -> None:
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    @staticmethod
    def has_model(
        model: str,
    ) -> bool:

        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
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