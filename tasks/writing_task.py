# tasks/writing_task.py
from crewai import Task
from agents import creative_writer

# Task: Write the Video Script
writing_task = Task(
    description=(
        "Based on the research report, select the most promising topic and write a "
        "script for a 16-second YouTube Short. The script must be engaging, clear, "
        "and easy for a beginner to understand. It should include a catchy title."
    ),
    expected_output=(
        "A final video script text that includes: "
        "1. A compelling Title. "
        "2. The full voiceover script."
    ),
    agent=creative_writer
)