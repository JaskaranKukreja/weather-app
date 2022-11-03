from flask import Blueprint,request,make_response,jsonify

from weather_app.util import exception_handler,NotFoundError,ValidationError

from weather_app.data_access.city import get_city_by_name,get_city_by_coordinates
from weather_app.data_access.weather import get_prediction_data,get_max_min_temp_per_day

weather = Blueprint('weather', __name__,static_folder="static")

@weather.route("/weather/predict",methods=["GET"])
@exception_handler
def get_weather_predicton():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    city = request.args.get('city')
    
    weather_forecast_data = {}
    
    if city:
        city = get_city_by_name(city.upper())
        if not city:
            raise NotFoundError("Sorry! no weather forecast found for this city")
        weather_forecast_data = get_prediction_data(city.latitude,city.longitude) or {}
    elif latitude and longitude:
        weather_forecast_data = get_prediction_data(latitude,longitude) or {}
    else:
        raise ValidationError("Invalid query params")
    
    #Trim data
    trimmed_weather_forecast_data = {}
    for date, period_grouped_data in weather_forecast_data.items():
        trimmed_weather_forecast_data[date] = {}
        for period,data in period_grouped_data.items():
            trimmed_weather_forecast_data[date][period] = {
                'temperature': data['temperature']['value'],
                'feelsLike': data['feelsLike'],
                'pop': data['pop'],
                'weatherCode': data['weatherCode']['value'],
                'wind': str(data['wind']['speed'])+" "+data['wind']['direction']
            }
    return trimmed_weather_forecast_data

@weather.route("/weather/history",methods=["GET"])
@exception_handler
def get_weather_history():
    # For now, this API limits just sending max and min temperature per day. 
    # But can be extended for other usercases.
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    city = request.args.get('city')
    
    weather_forecast_data = {}
    
    if city:
        city = get_city_by_name(city.upper())
        if not city:
            raise NotFoundError("Sorry! no weather forecast found for this city")
        weather_forecast_data = get_max_min_temp_per_day(city.id) or {}
    elif latitude and longitude:
        city = get_city_by_coordinates(latitude, longitude)
        weather_forecast_data = get_max_min_temp_per_day(city.id) or {}
    else:
        raise ValidationError("Invalid query params")
    
    response = {}
    
    for date,max_temp,min_temp in weather_forecast_data:
        response[date] = {
            'date': date,
            'maxTemp': max_temp,
            'minTemp': min_temp
        }
    return response