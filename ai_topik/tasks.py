from crewai.project import CrewBase, task, crew
from crewai import Task, Agent
from .schemas.response_model import PreInput

@CrewBase
class Tasks:
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        pass
    
    def topik_preprocessing_task(self, agent: Agent) -> Task:
        """
        Example task that can be customized
        """
        return Task(
            config=self.tasks_config['topik_preprocessing_task'],
            agent=agent,
            output_file=f"output/preprocess.txt",
            output_pydantic=PreInput
        )
    
    def topik_question_task(self, agent: Agent) -> Task:
        """
        Example task that can be customized
        """
        return Task(
            config=self.tasks_config['topik_question_task'],
            agent=agent,
            output_file=f"output/example_output.xml"
        )

