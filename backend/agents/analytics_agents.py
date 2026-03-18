import os
from agent_base import BaseAgent
from models import AgentRequest, AgentResponse

class SEOOptimizationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SEO Optimization",
            system_prompt="You are the SEO Optimization Agent. You generate optimized titles, YouTube descriptions, tags, and website metadata to maximize search rankings."
        )

class TrafficAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Traffic Analyst",
            system_prompt="You are the Traffic Analyst Agent. You ingest metrics from YouTube Analytics and Google Analytics to report on video performance, audience retention drops, and conversion rates."
        )

class TrendMonitorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Trend Monitor",
            system_prompt="You are the Trend Monitor Agent. You analyze current trends (Google Trends, social media) to suggest timely, high-potential topics for the next content cycle."
        )
