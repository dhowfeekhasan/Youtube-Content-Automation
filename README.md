
# Youtube Content Automation

This tool automates the entire short-video pipeline — from content research to scriptwriting and video generation — enabling faster output, reduced human effort, and consistent educational quality.

Sample Output : https://app.elai.io/v/6887d178c670805733d4d462

# Architecture Diagram

<img width="534" height="722" alt="image" src="https://github.com/user-attachments/assets/24db3aed-e904-49bd-ab61-54d61bcf25a4" />


# Project Structure 
    youtube-content-automation/
    │
    ├── main.py                     #  Main script: runs the full pipeline
    ├── config.py                   # API keys, model, and settings
    ├── .env                        # Stores secret API keys (not committed)
    ├── requirements.txt            #  Python dependencies
    │
    | agents/                       # 🧠 AI agents using CrewAI
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


# How to run the project 
📦1.Before starting, make sure you have:

- Python 3.8+

- Git installed

- A free account on:

Elai.io

Google Cloud Console (for YouTube Data API)

🔑2. API Keys Required:
| API                     | Use                                | Required For     |
| ----------------------- | ---------------------------------- | ---------------- |
| **YouTube Data API v3** | Fetch trending educational videos  | Research agent   |
| **Elai.io API**         | Generate AI-avatar narrated videos | Video generation |

🌐 3. API Key Setup & Links

i . Steps for YouTube Data API

- Create a project

- Enable YouTube Data API v3

- Go to APIs & Services > Credentials

- Click “+ Create Credentials” → API Key

📌 Copy your key (looks like AIza...)
💡 You’ll use this in the .env file as YOUTUBE_API_KEY

ii. Steps for Elai.io API
🔗 Elai API Docs

🔗 Elai Dashboard

- Sign up at https://elai.io

- Go to Dashboard → Integrations → API Access

- Copy the API Key

📌 Use this in your .env file as ELAI_API_KEY 

🗂️ 4. Project Setup (Windows Example)

🔹 Step 1: Create a Virtual Environment

    python -m venv venv
    venv\Scripts\activate
🔹 Step 2: Install Python Dependencies
        
    pip install -r requirements.txt
🔹 Step 3: Set Up .env File
Create a .env file in the root folder:

    YOUTUBE_API_KEY=your_youtube_api_key_here
    ELAI_API_KEY=your_elai_api_key_here

Step 5. Run the Automation Pipeline
Once everything is configured:

    python main.py
 

