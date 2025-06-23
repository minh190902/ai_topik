import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from dotenv import load_dotenv
load_dotenv(".env", override=True)

from ai_topik.crew import AIVocabExpansionCrew
import time

print("Starting AI Learning Crew...")
start_time = time.time()
crew = AIVocabExpansionCrew()
inputs = {
    "model_provider": "openai",
    "model_id": "gpt-4o-mini",
    "temperature": 0.5,
    "level": "Trung cấp",
    "type": "Ngữ pháp",
    "subtype": "tìm ý chính",
    "topic": "thú cưng",
}

# Run the planning kickoff
results = crew.topik_question_crew(inputs)
print(results)
# print("---")
# print(results.raw)
print("AI Learning Crew planning completed successfully. Tasks executed in {:.2f} seconds.".format(time.time() - start_time))
    