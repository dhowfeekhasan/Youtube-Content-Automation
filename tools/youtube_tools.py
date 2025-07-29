import os
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from crewai.tools import tool
from config import Youtube_REGION, YOUTUBE_MAX_RESULTS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@tool("YouTube Trending Topic Search")
def Youtube_tool(search_query: str) -> str:
    """Searches YouTube for a given query to find trending topics."""
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        return "Error: YouTube API Key is not configured."

    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        # DEFINITIVE FIX: The correct syntax is Youtube().list()
        request = youtube().list(
            part="snippet",
            q=search_query,
            type="video",
            videoCategoryId="27",
            regionCode=Youtube_REGION,
            order="viewCount",
            maxResults=YOUTUBE_MAX_RESULTS
        )
        response = request.execute()
        titles = [item['snippet']['title'] for item in response.get('items', [])]
        
        if not titles:
            return f"No trending videos found for the query '{search_query}'."
            
        return "\n".join(titles)

    except HttpError as e:
        return f"An HTTP error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"