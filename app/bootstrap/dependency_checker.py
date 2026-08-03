from app.bootstrap.ollama_manager import OllamaManager
from app.config.settings import settings


class DependencyChecker:

    @staticmethod
    def check() -> None:

        if not OllamaManager.is_installed():
            raise RuntimeError(
                "Ollama is not installed."
            )

        if not OllamaManager.is_running():
            OllamaManager.start()

        if not OllamaManager.has_model(
            settings.ollama_model,
        ):
            OllamaManager.pull_model(
                settings.ollama_model,
            )