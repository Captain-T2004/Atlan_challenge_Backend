# Travel Itinerary Generator Backend

This is the FastAPI backend for the Travel Itinerary Generator application. It uses Google's Generative AI to create personalized travel itineraries based on user preferences.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)


## Features

- RESTful API endpoint for generating travel itineraries
- Integration with Google's Generative AI (Gemini 1.5 Flash model)
- Custom prompt generation based on user preferences
- Logging for better debugging and monitoring

## Technologies Used

- FastAPI
- Pydantic for data validation
- Google Generative AI
- Python-dotenv for environment management
- Uvicorn as the ASGI server

## Prerequisites

- Python 3.7+
- A Google API key for the Generative AI service

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/travel-itinerary-backend.git
   cd travel-itinerary-backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install fastapi pydantic google-generativeai python-dotenv uvicorn
   or
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.

3. Use the `/generate_itinerary` endpoint to generate travel itineraries:
   ```
   POST /generate_itinerary
   ```
   Request body should follow the `TravelPreferences` model defined in the code.

## API Endpoints

### POST /generate_itinerary

Generates a travel itinerary based on user preferences.

Request body:
```json
{
  "travel_type": "string",
  "budget": 0,
  "local_budget": 0,
  "interests": ["string"],
  "trip_duration": 0,
  "number_of_travelers": 0,
  "traveling_with_children": true,
  "preferred_weather": ["string"],
  "other_requirements": "string",
  "residence_country": "string",
  "number_of_children": 0,
  "currency": "string"
}
```

Response:
```json
{
  "locations": ["string"],
  "details": "string"
}
```

## Error Handling

The API returns a 500 status code with an error message in case of any exceptions during the itinerary generation process.

## Development

- The main application logic is contained in a single file (`main.py`).
- The `generate_prompt` function creates a custom prompt for the AI model based on user preferences.
- The `/generate_itinerary` endpoint processes the user's travel preferences and returns a generated itinerary.

## Contact

[Akshay Behl](https://www.linkedin.com/in/akshay-behl-450661258/), akshaybehl213@outlook.com

Project Link: [https://github.com/your-username/travel-itinerary-backend](https://github.com/your-username/travel-itinerary-backend)
