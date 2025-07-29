# tasks/video_task.py
#This agent is for future purpose . This is not part of this project 
from crewai import Task
from agents.video_producer import video_producer


video_task = Task(
    description="Use the script to generate a video using Elai.io",
    expected_output="Final video rendered and downloaded locally in mp4 format.",
    agent=video_producer,
    async_execution=False,
    output_file="outputs/video_output.mp4",
)
