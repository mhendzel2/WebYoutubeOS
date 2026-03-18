import os
import json
from models import AgentRequest, AgentResponse
import litellm

class BaseAgent:
    """Base class for all Specialized Web and YouTube Management Agents."""
    
    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        
        # Determine the best model based on configured API keys for maximum flexibility
        if os.getenv("OPENROUTER_API_KEY"):
            self.default_model = "openrouter/anthropic/claude-3-haiku"
        elif os.getenv("ANTHROPIC_API_KEY"):
            self.default_model = "claude-3-haiku-20240307"
        elif os.getenv("OPENAI_API_KEY"):
            self.default_model = "gpt-4o-mini"
        elif os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
            self.default_model = "gemini/gemini-1.5-pro"
        else:
            # Drop back to local Ollama if no keys are provided
            self.default_model = "ollama/llama3"

    async def process(self, request: AgentRequest) -> AgentResponse:
        """
        Process user input and application context to generate an agent-specific response.
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": request.user_input}
        ]
        
        # In a real app we'd inject `request.context` intelligently into messages.
        if request.context:
            messages.insert(1, {"role": "system", "content": f"Context: {json.dumps(request.context)}"})

        try:
            # Subclasses can override self.model_name for specific high-performance needs
            model_to_use = getattr(self, "model_name", self.default_model)
            
            # Setup specific routing for local ollama
            api_base = "http://localhost:11434" if model_to_use.startswith("ollama/") else None
            
            completion = await litellm.acompletion(
                model=model_to_use,
                messages=messages,
                temperature=0.7,
                api_base=api_base
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
