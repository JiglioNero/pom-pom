#!flask/bin/python
from flask import Flask
from flask import request
import weather_api as Api

app = Flask(__name__)


@app.route('/current')
def current():
    return Api.get_current_weather(define_args(request.args))


@app.route('/forecast')
def forecast():
    return Api.get_forecast_5d3h_weather(define_args(request.args))


def define_args(args):
    city = args.get('city')
    lat = args.get('lat')
    lon = args.get('lon')
    if city:
        return {'q': city}
    else:
        return {'lat': lat,
                'lon': lon}
