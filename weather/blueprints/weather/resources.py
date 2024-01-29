from flask import request, jsonify
from flask_restful import Resource

from weather.use_cases.weather_use_case import GetWeatherUseCase
from weather.app import minimal_app
from weather.ext.database import init_app as db_init
from weather.repository import WeatherRespository


class WeatherResource(Resource):
    def get(self):
        app = minimal_app()
        db = db_init(app)
        result = WeatherRespository(db.weather).get_all()
        return jsonify(result)
    
    def post(self):
        data = request.get_json(force=True)
        app = minimal_app()
        db = db_init(app)
        res_use_case = GetWeatherUseCase().get_weather_use_case(lat=data.get("lat"), lon=data.get("long"))
        result = WeatherRespository(db.weather).insert(res_use_case)
        return jsonify(
            {"status": True, "result": result}
        )
