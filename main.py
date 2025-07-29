import os
import datetime
from agents.market_researcher import market_researcher
from agents.creative_writer import creative_writer
from crewai import Crew, Process
from tasks.research_task import research_task
from tasks.writing_task import writing_task
from tools.elai_video_generator import ElaiVideoGeneratorTool

# Step 1: Create timestamped output folder
current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"outputs/run_{current_time}"
os.makedirs(output_dir, exist_ok=True)

# Step 2: Run CrewAI agents
crew = Crew(
    agents=[market_researcher, creative_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True
)
crew_result = crew.kickoff()

# Step 3: Save the script to file
script_text = str(crew_result)
script_path = os.path.join(output_dir, "script.txt")
with open(script_path, "w", encoding="utf-8") as f:
    f.write(script_text)
print(f"✅ Script saved to: {script_path}")

# Step 4: Generate video using Elai
if script_text.strip():
    title = "Educational Shorts Video"
    video_generator = ElaiVideoGeneratorTool()
    result = video_generator.run(title, script_text)
    print("🎉 Final video saved to:", result)
else:
    print("❌ Script is empty. Cannot send to Elai API.")
