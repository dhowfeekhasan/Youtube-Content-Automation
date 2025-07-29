# tasks/research_task.py
from crewai import Task
from agents import market_researcher
from tools.youtube_tools import Youtube_tool 
from config import Youtube_QUERY

# Task: Find Trending Topics
research_task = Task(
    description=(
        f"Use the YouTube Trending Topic Search tool to find popular videos about '{Youtube_QUERY}'. "
        "Analyze the results and identify 1 key themes or video ideas. "
        "Focus on clarity and present a concise report of your findings."
    ),
    expected_output=(
        "A bullet-point list of 1 trending educational video topics, along with a "
        "brief explanation for each. This report will be used by the Creative Writer."
    ),
    agent=market_researcher,
    tools=[Youtube_tool] # Assign tool here
)