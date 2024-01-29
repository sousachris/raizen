from weather.external_interfaces import call_api
from weather.dto import WeatherInsert
from datetime import date


class GetWeatherUseCase():

    def get_weather_use_case(self, lat: float, lon: float):
        res_api = call_api(lat, lon)
        today = date.today().strftime('%d/%m/%Y')
        weather = WeatherInsert(data=res_api, created_at=today).to_json()
        return weather