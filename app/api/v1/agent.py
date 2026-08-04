from fastapi import APIRouter
from pydantic import BaseModel

from app.core.dependencies import agent_runtime


router = APIRouter()


class AgentRequest(BaseModel):
    prompt: str


@router.post("/agent")
async def run_agent(
    request: AgentRequest,
):

    response = await agent_runtime.run(
        request.prompt,
    )

    return {
        "response": response,
    }