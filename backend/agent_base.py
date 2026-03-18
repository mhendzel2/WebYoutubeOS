import os
from openai import AsyncOpenAI
from models import AgentRequest, AgentResponse
import json

class BaseAgent:
    """Base class for all Specialized Web and YouTube Management Agents."""
    
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        # Support local Ollama or OpenAI
        api_key = os.getenv("OPENAI_API_KEY", "")
        if api_key:
            self.client = AsyncOpenAI(api_key=api_key)
            self.model_name = "gpt-4o"
        else:
            # Drop back to local Ollama. Ensure Ollama is running (`ollama serve`)
            self.client = AsyncOpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama"  # required but unused
            )
            self.model_name = "llama3" # A safe default for local generation

    async def process(self, request: AgentRequest) -> AgentResponse:
        """
        Process user input and application context to generate an agent-specific response.
        This provides a default implementation that can be overridden by subclasses.
        """
        if not self.client:
           return AgentResponse(
               agent_name=self.name, 
               content="Failed to initialize AI client. Check your API settings.",
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
