import json

from redis_db import get_redis_connection
from sql_db import session
from sqlalchemy import func

from weather_app.data_models import Weather,City

def get_prediction_data(latitude,longitude):
    redis = get_redis_connection()
    forecast_data = redis.get(f'({latitude},{longitude})')
    return json.loads(forecast_data.decode('utf-8'))

def get_max_min_temp_per_day(city_id):
    return session.query(
        Weather.date.label('date'),
        func.max(Weather.temperature).label('max_temp'),
        func.min(Weather.temperature).label('min_temp')
    ).filter(
        Weather.city_id == city_id,
    ).group_by(
        Weather.date
    ).order_by(
        Weather.date
    ).all()
    