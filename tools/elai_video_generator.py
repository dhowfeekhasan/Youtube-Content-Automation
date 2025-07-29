# tools/elai_tools.py

import os
import requests
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ELAI_API_KEY = os.getenv("ELAI_API_KEY")
ELAI_HEADERS = {
    "Authorization": f"Bearer {ELAI_API_KEY}",
    "Content-Type": "application/json"
}

# Class wrapper for CrewAI usage
class ElaiVideoGeneratorTool:
    def __init__(self):
        pass

    def run(self, title, script_text):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"outputs/run_{timestamp}"
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, "final_video_elai.mp4")
        generate_elai_video(script_text, output_path)
        return output_path

def generate_elai_video(script_text: str, output_path: str):
    try:
        # 1. Create video
        create_url = "https://apis.elai.io/api/v1/videos"
        payload = {
            "name": "YouTube Script Video",
            "slides": [
                {
                    "id": 1,
                    "canvas": {
                        "objects": [
                            {
                                "type": "avatar",
                                "left": 150,
                                "top": 20,
                                "fill": "#4868FF",
                                "scaleX": 0.37,
                                "scaleY": 0.37,
                                "height": 1080,
                                "width": 1080,
                                "src": "https://elai-media.s3.eu-west-2.amazonaws.com/avatars/jade.png",
                                "avatarType": "transparent",
                                "animation": {"type": None}
                            }
                        ],
                        "background": "#ffffff",
                        "version": "4.4.0"
                    },
                    "avatar": {
                        "code": "jade",
                        "gender": "female"
                    },
                    "animation": "fade_in",
                    "language": "English",
                    "speech": script_text,
                    "voice": "en-US-AriaNeural",
                    "voiceType": "text",
                    "voiceProvider": "azure"
                }
            ],
            "tags": ["automation", "genai"],
            "public": False,
            "verified": False
        }

        response = requests.post(create_url, headers=ELAI_HEADERS, json=payload)
        response.raise_for_status()

        video_data = response.json()
        video_id = video_data["_id"]
        print(f"✅ Video created. ID: {video_id}")

        # 2. Trigger rendering
        render_url = f"https://apis.elai.io/api/v1/videos/render/{video_id}"
        render_resp = requests.post(render_url, headers=ELAI_HEADERS)
        render_resp.raise_for_status()
        print("🚀 Render triggered successfully.")

        # 3. Wait for render
        status_url = f"https://apis.elai.io/api/v1/videos/{video_id}"
        while True:
            time.sleep(10)
            status_resp = requests.get(status_url, headers=ELAI_HEADERS)
            status_data = status_resp.json()
            status = status_data.get("status")
            print(f"📺 Status: {status}")

            if status == "ready":
                download_url = status_data.get("url")
                preview = f"https://app.elai.io/preview/{video_id}"
                print(f"✅ Video ready! Preview: {preview}")
                break
            elif status == "failed":
                raise Exception("❌ Video rendering failed.")
        
        # 4. Download video
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        download_resp = requests.get(download_url, stream=True)
        with open(output_path, "wb") as f:
            for chunk in download_resp.iter_content(1024):
                f.write(chunk)
        print(f"⬇️ Downloaded to {output_path}")

    except Exception as e:
        print(f"❌ Error in generate_elai_video: {e}")

