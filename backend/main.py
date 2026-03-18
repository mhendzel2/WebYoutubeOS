from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import Dict, Any
import os

from models import AgentRequest, AgentResponse
from agents.brand_coordinator_agent import BrandCoordinatorAgent
from agents.scriptwriter_agent import ScriptwriterAgent
from agents.graphic_designer_agent import GraphicDesignerAgent
from agents.research_agent import ResearchAgent
from agents.audio_agent import AudioVoiceAgent
from agents.video_assembly_agent import VideoAssemblyAgent
from agents.editorial_agents import ScriptCriticAgent, VisualCriticAgent
from agents.analytics_agents import SEOOptimizationAgent, TrafficAnalystAgent, TrendMonitorAgent

load_dotenv()

app = FastAPI(title="YouTube & Web OS API", version="1.0.0")

# Configure CORS for our Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Agents
agents_registry = {
    "brand_coordinator": BrandCoordinatorAgent(),
    "scriptwriter": ScriptwriterAgent(),
    "graphic_designer": GraphicDesignerAgent(),
    "research": ResearchAgent(),
    "audio": AudioVoiceAgent(),
    "video_assembly": VideoAssemblyAgent(),
    "script_critic": ScriptCriticAgent(),
    "visual_critic": VisualCriticAgent(),
    "seo": SEOOptimizationAgent(),
    "traffic": TrafficAnalystAgent(),
    "trend": TrendMonitorAgent()
}

@app.get("/")
def read_root():
    return {"status": "ok", "message": "YouTube & Web OS API is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/agent/{agent_id}", response_model=AgentResponse)
async def query_agent(agent_id: str, request: AgentRequest):
    """
    Routes a request to the specified specialized agent.
    """
    if agent_id not in agents_registry:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")
        
    try:
        agent = agents_registry[agent_id]
        response = await agent.process(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
