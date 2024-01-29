from flask import Blueprint
from flask_restful import Api

from .resources import WeatherResource

bp = Blueprint("weather", __name__, url_prefix="/api")
api = Api(bp)


def init_app(app):
    api.add_resource(WeatherResource, "/weather")
    app.register_blueprint(bp)