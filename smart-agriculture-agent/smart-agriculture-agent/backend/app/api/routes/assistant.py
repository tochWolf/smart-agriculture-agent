from fastapi import APIRouter
from app.schemas import AssistantRequest
from app.agents.agriculture_agent import agriculture_agent

router = APIRouter(prefix="/api/assistant", tags=["AI Assistant"])

@router.post("/ask")
def ask_assistant(request: AssistantRequest):
    return agriculture_agent.answer(request.question, request.crop, request.location)
