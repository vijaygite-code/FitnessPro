
import logging
import os
from .gemini_api import _call_gemini_api
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

async def generate_progress_insight(context_summary: str) -> str:
    """
    Generates a short, personalized insight or motivational message based on the user's data context.
    """
    try:
        prompt = f"""
        You are an elite fitness coach.
        Analyze this user's recent workout data summary: "{context_summary}"
        
        If the trend is positive (progress up), give a short, high-energy compliment (max 2 sentences).
        If the trend is negative/flat, give a short, empathetic motivational quote about recovery and consistency (max 2 sentences).
        
        Do not use technical jargon. Be human, encouraging, and brief.
        """
        
        response = await _call_gemini_api(prompt)
        return response.strip()
        
    except Exception as e:
        logger.error(f"Error generating AI insight: {e}")
        return "Consistency is key! Keep showing up."
