import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class ScriptwriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scriptwriter",
            system_prompt="You are the Scriptwriter Agent. You generate complete, engaging YouTube scripts and SEO-optimized website blog drafts based on rough outlines provided by the user."
        )
        # Override default to use a high-performance OpenRouter model for dense writing tasks
        self.model_name = "anthropic/claude-3.5-sonnet"
