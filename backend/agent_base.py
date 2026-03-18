import os
from openai import AsyncOpenAI
from models import AgentRequest, AgentResponse
import json

class BaseAgent:
    """Base class for all Specialized Web and YouTube Management Agents."""
    
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        # OpenRouter Integration
        self.api_key = os.getenv("OPENROUTER_API_KEY", "")
        
        # We will use OpenRouter via the official OpenAI python package
        # OpenRouter's base URL is https://openrouter.ai/api/v1
        if self.api_key:
            self.client = AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=self.api_key,
            )
            # Default to a high tier price/performance model unless overridden
            self.model_name = "anthropic/claude-3-haiku" 
        else:
            # Fallback to local Ollama ONLY if OpenRouter key is missing
            self.client = AsyncOpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama" 
            )
            self.model_name = "llama3"

    async def process(self, request: AgentRequest) -> AgentResponse:
        """
        Process user input and application context to generate an agent-specific response.
        This provides a default implementation that can be overridden by subclasses.
        """
        if not self.api_key and self.model_name != "llama3":
           return AgentResponse(
               agent_name=self.name, 
               content="OPENROUTER_API_KEY is not configured.",
               confidence=0.0
           )

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": request.user_input}
        ]
        
        # In a real app we'd inject `request.context` intelligently into messages.
        if request.context:
            messages.insert(1, {"role": "system", "content": f"Context: {json.dumps(request.context)}"})

        try:
            completion = await self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
            )
            
            return AgentResponse(
                agent_name=self.name,
                content=completion.choices[0].message.content or "",
                confidence=0.9
            )
        except Exception as e:
            return AgentResponse(
                agent_name=self.name,
                content=f"Error generating response: {str(e)}",
                confidence=0.0
            )
