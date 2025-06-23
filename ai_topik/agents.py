from crewai import Agent, LLM
from crewai.project import CrewBase, agent, crew, task

from langchain_openai import ChatOpenAI

from .model_provider_manager import provider_config, llm_key_manager

@CrewBase
class Agents:
    agents_config = 'config/agents.yaml'
    
    def __init__(self) -> None:
        pass
    def get_client(
            self,
            model_provider: str = "openai",
            model_id: str = None,
            **kwargs
        ):
            """
            Initialize client using ChatOpenAI
            """
            config = provider_config.get_provider_config(
                provider=model_provider,
                secret_manager=llm_key_manager
            )
            model_id = model_id if model_id else config["default_model"]
            
            client = ChatOpenAI(
                model=model_id,
                base_url=config["base_url"],
                api_key=config["api_key"],
                **{k: v for k, v in kwargs.items() if k not in ["model"]}
            )
            return client
    
    def get_llm(
        self, 
        model_provider: str = "openai", 
        model_id: str = None, 
        temperature: int = 0.5, 
        repeat_penalty: int = 1.1,
        **kwargs
    ) -> LLM:
        """
        Initialize llm using LLM
        Params:
        - model_id: ID for a specific LLM
        """
        config = provider_config.get_provider_config(
            provider=model_provider,
            secret_manager=llm_key_manager
        )
        model_id = model_id if model_id else config["default_model"]
        
        return LLM(
            model=f"{model_provider}/{model_id}",  # Model ID
            api_key=config["api_key"],
            **{k: v for k, v in kwargs.items() if k not in ["model"]},
        )
    
    def topik_question_agent(
        self,
        model_provider: str = "openai",
        model_id: str = None,
        **kwargs
    ) -> Agent:
        """
        Create a vocabulary expansion agent
        """
        return Agent(
            config=self.agents_config["topik_question_agent"],
            llm=self.get_llm(
                model_provider, 
                model_id, 
                **kwargs
            ),
        )