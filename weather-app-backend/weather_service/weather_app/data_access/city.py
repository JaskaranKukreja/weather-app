from sql_db import session

from weather_app.data_models.city import City

def get_city_by_name(city_name):
    return session.query(City).filter(
        City.name == city_name
    ).one_or_none()

def get_city_by_coordinates(latitude,longitude):
    return session.query(City).filter(
        City.latitude == latitude,
        City.longitude == longitude
    ).one_or_none()