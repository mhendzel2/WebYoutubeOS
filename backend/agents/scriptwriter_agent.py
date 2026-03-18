import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class ScriptwriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Scriptwriter",
            system_prompt="You are the Scriptwriter Agent. You generate complete, engaging YouTube scripts and SEO-optimized website blog drafts based on rough outlines provided by the user."
        )
        # Override default to use a high-performance model for dense writing tasks
        if os.getenv("OPENROUTER_API_KEY"):
            self.model_name = "openrouter/anthropic/claude-3.5-sonnet"
        elif os.getenv("ANTHROPIC_API_KEY"):
            self.model_name = "claude-3-5-sonnet-20240620"
        elif os.getenv("OPENAI_API_KEY"):
            self.model_name = "gpt-4o"
        elif os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
            self.model_name = "gemini/gemini-1.5-pro"
