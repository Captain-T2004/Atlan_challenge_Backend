from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

class TravelPreferences(BaseModel):
    travel_type: str
    budget: float
    local_budget: float
    interests: List[str]
    trip_duration: int
    number_of_travelers: int
    traveling_with_children: bool
    preferred_weather: List[str]
    other_requirements: Optional[str] = None
    residence_country: Optional[str] = None
    number_of_children: Optional[int] = None
    currency: Optional[str] = None

class Itinerary(BaseModel):
    locations: List[str]
    details: str

def generate_prompt(preferences: TravelPreferences) -> str:
    return f"""Generate a detailed travel itinerary based on the following preferences:
    Residence Country: {preferences.residence_country or 'INTERNATIONAL'}
    Travel Type: {preferences.travel_type}
    Budget: ${preferences.budget}
    local budget: ${preferences.local_budget}
    currency: ${preferences.currency or 'USD'}
    Interests: {', '.join(preferences.interests)}
    Trip Duration: {preferences.trip_duration} days
    Number of Travelers: {preferences.number_of_travelers}
    Traveling with Children: {'Yes' if preferences.traveling_with_children else 'No'}
    Number of Children: {preferences.number_of_children if preferences.traveling_with_children else '0'}
    Preferred Weather: {', '.join(preferences.preferred_weather)}
    Other Requirements: {preferences.other_requirements or 'None'}

    Also please give some recommendations for the hotels too.
    Please consider current world events, travel restrictions, and seasonal factors when suggesting destinations and activities.
    Provide a list of recommended locations and a detailed day-by-day itinerary.
    """

@app.post("/generate_itinerary", response_model=Itinerary)
async def generate_itinerary(preferences: TravelPreferences):
    try:
        prompt = generate_prompt(preferences)
        logger.info(f"Generating itinerary for preferences: {preferences}")
        
        response = model.generate_content(prompt)
        
        itinerary_text = response.text
        locations = [line.split(':')[0] for line in itinerary_text.split('\n') if ':' in line][:5]
        
        logger.info(f"Successfully generated itinerary with {len(locations)} locations")
        return Itinerary(
            locations=locations,
            details=itinerary_text
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)