import requests
from typing import Dict, Any
from .base_tool import BaseTool
from config.settings import settings

class WeatherTool(BaseTool):
    def __init__(self):
        super().__init__('WeatherTool')
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.api_key = settings.openweather_api_key
    
    def execute(self, city_name: str, **kwargs) -> Dict[str, Any]:
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
