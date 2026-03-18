from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AgentRequest(BaseModel):
    session_id: str
    user_input: str
    context: Optional[Dict[str, Any]] = None

class AgentResponse(BaseModel):
    agent_name: str
    content: str
    action_items: Optional[List[str]] = None
    confidence: float = 1.0

class ManuscriptChunk(BaseModel):
    chunk_id: str
    text: str
    entities_detected: List[str] = []
    
class ContextUpdate(BaseModel):
    new_characters: List[str] = []
    new_locations: List[str] = []
    plot_points: List[str] = []
