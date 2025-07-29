# agents/video_producer.py 
#This agent is for future purpose . This is not part of this project 
from crewai import Agent
from config import MODEL_NAME
# Agent: Video Producer
video_producer = Agent(
    role='Digital Media Producer',
    goal='Take a script and an avatar image to produce a final video file.',
    backstory=(
        "You are a tech-savvy producer who bridges the gap between creative content and "
        "final production. You are an expert at using AI tools to bring scripts to life."
    ),
    llm=MODEL_NAME, # Use the explicit llm object
    verbose=True,
    allow_delegation=False
)
