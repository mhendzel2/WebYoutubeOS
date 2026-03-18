import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class ScriptCriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Script Critic",
            system_prompt="You are the Script Critic Agent. Review YouTube drafts for hook strength, viewer retention tactics, pacing, and clarity before production begins."
        )

class VisualCriticAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Visual Critic",
            system_prompt="You are the Video & Visual Critic Agent. Review storyboard, thumbnails, and visual asset alignment with the script to ensure high production value."
        )
