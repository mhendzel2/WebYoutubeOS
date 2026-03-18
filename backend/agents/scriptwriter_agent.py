import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class ScriptwriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scriptwriter",
            system_prompt="You are the Scriptwriter Agent for YouTube and Web Management OS. You write high-retention, engaging YouTube video scripts and SEO-optimized website articles. You always adhere strictly to the guidelines passed by the Brand Coordinator."
        )
