from pydantic import BaseModel


class WorkflowResponse(BaseModel):
    workflow_id: str
    status: str
    result: dict