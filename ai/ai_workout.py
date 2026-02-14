import os
import logging
import httpx
from typing import List, Optional
from pydantic import BaseModel
from .. import schemas, models
from .gemini_api import _call_gemini_api

logger = logging.getLogger(__name__)

class WorkoutPlanRequest(BaseModel):
    days_per_week: int
    duration_minutes: int
    fitness_level: str # Beginner, Intermediate, Advanced
    equipment: Optional[str] = "Gym equipment"
    focus_area: Optional[str] = "Full Body"

async def generate_workout_plan(user: models.User, request: WorkoutPlanRequest) -> str:
    """Generates a personalized workout plan."""
    
    prompt = f"""
    Act as an elite personal trainer. Create a personalized {request.days_per_week}-day weekly workout plan for a client with the following profile:

    **Client Profile:**
    - Age: {user.age}
    - Weight: {user.weight} kg
    - Height: {user.height} cm
    - Goal: {user.goals}
    
    **Preferences:**
    - Days per week: {request.days_per_week}
    - Duration per session: {request.duration_minutes} minutes
    - Fitness Level: {request.fitness_level}
    - Equipment Access: {request.equipment}
    - Focus Area: {request.focus_area}

    **Instructions:**
    - Provide a structured plan for each day (Day 1, Day 2, etc.).
    - Include exercises, sets, reps, and brief rest instructions.
    - Provide a warm-up and cool-down routine.
    - Give a brief nutritional tip based on their goal.
    - Format usage of Markdown is encouraged for readability.
    """
    
    return await _call_gemini_api(prompt)
