import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse
from agents.browser_toolkit import BrowserToolkit

class GraphicDesignerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Graphic Designer",
            system_prompt="You are the Graphic Designer Agent. You interface with Google Slides via the custom AI Browser API to programmatically generate presentation graphics, YouTube thumbnails, and visual assets based on script requirements."
        )
        self.browser = BrowserToolkit()
        
    async def process(self, request: AgentRequest) -> AgentResponse:
        """Override to implement browser interaction for Google Slides."""
        if "generate slide" in request.user_input.lower() or "thumbnail" in request.user_input.lower():
            # Example heuristic: actually tell the browser to do something
            # First ensure browser is open
            status = self.browser.check_status()
            if status.get("status") == "offline":
                return AgentResponse(agent_name=self.name, content="Browser API is offline. Cannot generate graphics.", confidence=0.0)
                
            return AgentResponse(
                agent_name=self.name,
                content="Acknowledged. In a full implementation, I would navigate to Google Slides and generate the requested assets.",
                confidence=0.8
            )
            
        # Fallback to the base LLM process
        return await super().process(request)
