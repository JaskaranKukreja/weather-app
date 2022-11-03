import requests
import json

from flask import Flask,request,redirect
from sql_db import init_sql_db,session
from redis_db import get_redis_connection

from weather_app.data_models import City,Weather

from weather_app.controller.weather import weather


app = Flask(__name__)

init_sql_db()

# Register blueprint(s)
app.register_blueprint(weather)

# TODO: Redirect index route to swagger-ui
@app.route("/")
def index():
    return "Hello word..."
