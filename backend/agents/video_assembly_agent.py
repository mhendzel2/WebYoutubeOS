import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class VideoAssemblyAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Video Assembly",
            system_prompt="You are the Video Assembly Agent. You act as the final coordinator, taking the written script, generated audio files, and Google Slides graphics to map out the final video timeline. You output detailed EDL/XML logic for Premiere Pro, or programmatic rendering instructions for FFmpeg."
        )
        
    async def process(self, request: AgentRequest) -> AgentResponse:
        """Process video rendering or timeline assembly requests."""
        if "assemble" in request.user_input.lower() or "render" in request.user_input.lower() or "timeline" in request.user_input.lower():
            return AgentResponse(
                agent_name=self.name,
                content="Video assembly pipeline triggered. I am compiling the visual assets and audio track into a master timeline.",
                confidence=0.95
            )
            
        return await super().process(request)
