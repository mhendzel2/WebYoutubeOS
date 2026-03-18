import os
import requests
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class AudioVoiceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Audio & Voice",
            system_prompt="You are the Audio and Voice Agent. You manage Text-to-Speech generation, audio pacing, and background music selection using local open-source models (via Ollama or similar local inferencing endpoints)."
        )
        # Local inference endpoint configured by user
        self.local_tts_url = "http://localhost:11434/api/generate"
        
    async def process(self, request: AgentRequest) -> AgentResponse:
        """Override to implement local TTS / Audio generation."""
        if "voice" in request.user_input.lower() or "audio" in request.user_input.lower() or "tts" in request.user_input.lower():
            # A mock call to a local model endpoint
            try:
                # We do a quick check to see if Ollama or the local endpoint is up
                # By default, Ollama responds to GET / exactly with "Ollama is running"
                res = requests.get("http://localhost:11434/")
                if res.status_code == 200:
                    return AgentResponse(
                        agent_name=self.name,
                        content=f"Local model endpoint detected. I will route the script through the local TTS generator.",
                        confidence=0.9
                    )
            except requests.exceptions.ConnectionError:
                return AgentResponse(
                    agent_name=self.name,
                    content="Local model endpoint (Ollama/TTS) is offline. Please start your local inference server.",
                    confidence=0.0
                )
                
            return AgentResponse(
                agent_name=self.name,
                content="Acknowledged. Audio processing request queued.",
                confidence=0.8
            )
            
        return await super().process(request)
