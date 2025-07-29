# agents/market_researcher.py
from crewai import Agent
from config import MODEL_NAME

# Agent: Market Researcher
market_researcher = Agent(
    role='Senior Market Analyst for YouTube Educational Content',
    goal='Find trending educational topics on YouTube in the specified region and identify key themes.',
    backstory=(
        "You are an expert at understanding YouTube trends. You use data to find "
        "what topics are currently capturing the audience's attention, focusing on the "
        "educational sector."
    ),
    # NO 'tools' parameter here
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)