from requests import get
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')
URL = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'api_key': API_KEY 
}

class OpenWeather:

    def get_data(self):
        res = get(f"{URL}/", params)
        res.raise_for_status()
        data = res.json()
