from typing import Iterator, AsyncGenerator, Dict, Any

from crewai import Crew, Process
from crewai.task import TaskOutput

from .agents import Agents
from .tasks import Tasks

from .utils.cache_service import SimpleCacheService

class AIVocabExpansionCrew:
    def __init__(self) -> None:
        # Init agents and tasks
        self.agents = Agents()
        self.tasks = Tasks()
        self.cache = SimpleCacheService(ttl=3600) 
    
    def topik_question_crew(self, inputs: Dict[str, Any]) -> str:
        """
        Run full end-to-end planning process
        """
        # Initialize Agents
        topik_question_agent = self.agents.topik_question_agent(
            model_provider=inputs["model_provider"],
            model_id=inputs["model_id"],
            temperature=0,
        )
        
        # Initialize Tasks
        preprocess_task = self.tasks.topik_preprocessing_task(topik_question_agent)
        topik_question_task = self.tasks.topik_question_task(topik_question_agent)
        end2end_crew = Crew(
            name="End-to-End Vocab Expansion Crew",
            agents=[topik_question_agent],
            tasks=[preprocess_task, topik_question_task],
            verbose=True,
        )
        # Kickoff the crew
        input_crew = {
            "level": inputs["level"],
            "type": inputs["type"],
            "subtype": inputs["subtype"],
            "topic": inputs["topic"],
        }
        end2end_result = end2end_crew.kickoff(inputs=input_crew)
        if not end2end_result:
            raise Exception("End-to-end crew failed to complete tasks")
        
        return end2end_result.raw