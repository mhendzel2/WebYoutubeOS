import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse
from agents.browser_toolkit import BrowserToolkit

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Deep Research",
            system_prompt="You are the Cinematic & Deep Research Agent. You interface with NotebookLM and the broader internet via the custom AI Browser API to digest source material, synthesize research, and assist in planning video structures."
        )
        self.browser = BrowserToolkit()
        
    async def process(self, request: AgentRequest) -> AgentResponse:
        """Override to implement browser interaction for NotebookLM/Web Research."""
        if "research" in request.user_input.lower() or "search" in request.user_input.lower():
            status = self.browser.check_status()
            if status.get("status") == "offline":
                return AgentResponse(agent_name=self.name, content="Browser API is offline. Cannot conduct deep research.", confidence=0.0)
                
            # Simulate a browser action
            return AgentResponse(
                agent_name=self.name,
                content="Acknowledged. I will trigger NotebookLM via the Browser API to synthesize the requested source material.",
                confidence=0.85
            )
            
        return await super().process(request)
