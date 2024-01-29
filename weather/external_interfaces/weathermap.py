from weather.utils import requests


URL = "https://api.openweathermap.org/"
KEY_TOKEN = "b18a601fab8ffaed2a0005e4967971c3"

def call_api(lat: float, lon: float):
    url = URL + f"data/2.5/forecast?lat={lat}&lon={lon}&lang=pt_br&appid={KEY_TOKEN}"
    return requests.call_api(url)
