from app.agent_runtime.conversation import Conversation
from app.llm.ollama_provider import OllamaProvider


class AgentExecutor:
    """
    Executes an AI conversation.
    MCP Host logic lives inside OllamaProvider.
    """

    def __init__(self):

        self._llm = OllamaProvider()

    async def chat(
        self,
        message: str,
    ) -> str:

        conversation = Conversation()

        conversation.user(message)

        response = await self._llm.chat(
            conversation.messages,
        )

        conversation.assistant(response)

        return response