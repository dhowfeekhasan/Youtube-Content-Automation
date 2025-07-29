This tool automates the entire short-video pipeline — from content research to scriptwriting and video generation — enabling faster output, reduced human effort, and consistent educational quality.
# Project Structure 
    youtube-content-automation/
    │
    ├── main.py                     #  Main script: runs the full pipeline
    ├── config.py                   # API keys, model, and settings
    ├── .env                        # Stores secret API keys (not committed)
    ├── requirements.txt            #  Python dependencies
    │
    | agents/                     # 🧠 AI agents using CrewAI
    │   ├── __init__.py
    │   ├── market_researcher.py    # → Finds trending YouTube topics
    │   └── creative_writer.py      # → Writes 30s spoken scripts
    │
    ├── tasks/                      #  Tasks assigned to agents
    │   ├── __init__.py
    │   ├── research_task.py        # → Assigns research job to agent
    │   └── writing_task.py         # → Assigns script-writing task
    │
    ├── tools/                      # 🔌 External API utilities
    │   ├── __init__.py
    │   ├── youtube_tools.py        # → YouTube Data API integration
    │   └── elai_video_generator.py # → Elai.io video generation API
    │
    ├── outputs/                    # 📤 Output folder for videos and scripts
    │   └── run_YYYYMMDD_HHMMSS/    # Timestamped subfolder per run
    │       ├── script.txt          # Generated voiceover script
    │       └── final_video.mp4     # Final video with AI narration
