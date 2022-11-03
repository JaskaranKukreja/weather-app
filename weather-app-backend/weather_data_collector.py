import requests
import json
import sqlite3

from time import sleep
from threading import Thread
from datetime import datetime
from redislite import Redis
from contextlib import closing

WAIT_PERIOD_TO_CALL_OBSERVATION_API = 60
WAIT_PERIOD_TO_CALL_SHORT_TERM_API = 300

BASE_URL = 'https://weatherapi.pelmorex.com/v1'

TOP_CANADIAN_CITIES = {
    'Toronto': (43.651070,-79.347015),'Montreal': (45.630001,-73.519997),'Ottawa': (45.424721,-75.695000),
    'Edmonton': (53.522778,-113.623055),'Winnipeg': (49.895077,-97.138451),'Vancouver':(49.246292,-123.116226)
}

def get_redis_connection():
    return Redis(".//redis.db")

def get_sql_connection():
    return sqlite3.connect(".//weather_app.db")

class DataAggregator:
    def __init__(self):
        pass
    
    def collect_short_term_weather_forecast_data(self):
        while True:
            for city,coordinates in TOP_CANADIAN_CITIES.items():
                try:
                    print(f"Calling collect_short_term_weather_forecast_data at for {city} time: {datetime.now()} .....")
                    response = requests.get(f"{BASE_URL}/shortterm?lat={coordinates[0]}&long={coordinates[1]}")
                    print(f"Received response for short_term_weather_forecast for {city} with length {len(response.json()['shortterm'])}")
                    with get_redis_connection() as redis_connection:
                        # Set key & value in redis
                        key=f"({coordinates[0]},{coordinates[1]})"
                        value={}
                        # Group data by periods for a given date
                        for weather_forecast in response.json()['shortterm']:
                            date = weather_forecast['time']['utc'].split("T")[0]
                            data = value.get(date,{})
                            data[f"period{weather_forecast['period']}"] = weather_forecast
                            value[date] = data
                        
                        redis_connection.set(key,json.dumps(value))
                        
                except Exception as exc:
                    print(f"An error occured while calling collect_short_term_weather_forecast_data for {city} with {exc}")  
            sleep(WAIT_PERIOD_TO_CALL_SHORT_TERM_API)

    def collect_current_weather_forecast_data(self):
        while True:
            for city,coordinates in TOP_CANADIAN_CITIES.items():
                try:
                    print(f"Calling collect_current_weather_forecast_data at for {city} time: {datetime.now()} .....")
                    response = requests.get(f"{BASE_URL}/observation?lat={coordinates[0]}&long={coordinates[1]}")
                    print(f"Received response from server for current weather for {city}")
                    
                    with get_sql_connection() as sql_connection:
                        weather_forecast = response.json()
                        # Get city id
                        city_id = sql_connection.execute(f"Select id from city where latitude = {coordinates[0]} and longitude = {coordinates[1]}").fetchone()
                        
                        recorded_time_stamp = datetime.strptime(weather_forecast['time']['utc'], '%Y-%m-%dT%H:%M')

                        if not sql_connection.execute(f"Select count(*) from weather where city_id = {city_id[0]} and recorded_datetime='{recorded_time_stamp}'").fetchone()[0]:
                            recorded_date = weather_forecast['time']['utc'].split("T")[0]
                            sql_query = f"""
                                INSERT INTO weather (city_id, date,recorded_datetime,weather_code,temperature,dew_point,feels_like,wind_direction,wind_speed,wind_gust,relative_humidity,pressure_value,pressure_trend,visibility,ceiling)
                                VALUES ({city_id[0]},'{recorded_date}','{recorded_time_stamp}','{weather_forecast['weatherCode']['value']}',{weather_forecast['temperature']},{weather_forecast['dewPoint']},
                                {weather_forecast['feelsLike']},'{weather_forecast['wind']['direction']}',{weather_forecast['wind']['speed']},{weather_forecast['wind']['gust']},{weather_forecast['relativeHumidity']},
                                {weather_forecast['pressure']['value']},{weather_forecast['pressure']['trend']},{weather_forecast['visibility']},{weather_forecast['ceiling']})                   
                            """
                            sql_connection.execute(sql_query)
                            sql_connection.commit()
                except Exception as exc:
                    print(f"An error occured while calling collect_current_weather_forecast_data for {city} with {exc}")  
            sleep(WAIT_PERIOD_TO_CALL_OBSERVATION_API)

    def run(self):
        print(f"Starting data-collector script at time: {datetime.now()} .....")
        
        #Start task1: collect current weather data
        current_weather_forecast_data_thread = Thread(
            target=self.collect_current_weather_forecast_data,
            name='current_weather_forecast_data_thread'
        )
        print(f"Starting current_weather_forecast_data_thread at time: {datetime.now()} .....")
        current_weather_forecast_data_thread.start()

        #Start task2: collect upcoming weather forecast data
        short_term_weather_forecast_data_thread = Thread(
            target=self.collect_short_term_weather_forecast_data,
            name='short_term_weather_forecast_data_thread'
        )
        print(f"Starting short_term_weather_forecast_data at time: {datetime.now()} .....")
        short_term_weather_forecast_data_thread.start()

if __name__ == '__main__':
    DataAggregator().run()