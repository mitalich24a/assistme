from fastapi import APIRouter

from app.agent_runtime.agent_executor import AgentExecutor
from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse

router = APIRouter()

executor = AgentExecutor()


@router.post(
    "/agent/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
):

    response = await executor.chat(
        request.message,
    )

    return ChatResponse(
        response=response,
    )