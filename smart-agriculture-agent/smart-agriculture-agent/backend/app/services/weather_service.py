import requests
from app.config import settings

def get_weather(city: str):
    if not settings.WEATHER_API_KEY:
        return {"available": False, "message": "Weather API key not configured."}

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": settings.WEATHER_API_KEY, "units": "metric"},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    return {
        "available": True,
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
    }
