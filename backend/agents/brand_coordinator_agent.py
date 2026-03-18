import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class BrandCoordinatorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Brand Coordinator",
            system_prompt="You are the Brand Coordinator Agent. You ensure that all generated outputs align with the specific tone, visual guidelines, and audience demographics of the selected target property (YouTube channel or Website). Analyze requests and enforce brand consistency."
        )
