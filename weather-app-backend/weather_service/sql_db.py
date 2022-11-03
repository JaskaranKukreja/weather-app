import os

from datetime import datetime

from sqlalchemy import create_engine,event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQL DB
db_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
engine = create_engine(f'sqlite:///{db_path}/weather_app.db')

session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = session.query_property()

def init_sql_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.
    
    from weather_app.data_models import City,Weather
    Base.metadata.create_all(bind=engine)

def seed_data():
    # Create cities table if not exists
    print("Creating tables......")
    session.execute("""
        CREATE TABLE IF NOT EXISTS city (
            id integer PRIMARY KEY AUTOINCREMENT,
            name varchar(200) NOT NULL,
            state varchar(200) NOT NULL,
            latitude float NOT NULL,
            longitude float NOT NULL,
            CONSTRAINT unique_city_full_address UNIQUE (name,state)
        )
        """
    )
    session.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id integer PRIMARY KEY AUTOINCREMENT,
            city_id integer NOT NULL,
            date varchar(20) NOT NULL,
            recorded_datetime datetime NOT NULL,
            weather_code varchar(20) NOT NULL,
            temperature float NOT NULL,
            dew_point float NOT NULL,
            feels_like float NOT NULL,
            wind_direction varchar(2) NOT NULL,
            wind_speed float NOT NULL,
            wind_gust float NOT NULL,
            relative_humidity float NOT NULL,
            pressure_value float NOT NULL,
            pressure_trend float NOT NULL,
            visibility float NOT NULL,
            ceiling float NOT NULL
        )
        """
    )
    session.commit()
    
    #Clean up all data
    session.execute("DELETE FROM city;")
    session.execute("DELETE FROM weather;")
    session.commit()
    
    #Insert initial data for cities
    city_data_queries = [
        ('TORONTO','ONTARIO',43.651070,-79.347015),
        ('MONTREAL','QUEBEC',45.630001,-73.519997),
        ('OTTAWA','ONTARIO',45.424721,-75.695000),
        ('EDMONTON','ALBERTA',53.522778,-113.623055),
        ('WINNIPEG','MANITOBA',49.895077,-97.138451),
        ('VANCOUVER','BRITISH COLUMBIA',49.246292,-123.116226)
    ]
    print("Inserting initial data into db......")
    for name,state,latitude,longitude in city_data_queries:
        session.execute(
            f"INSERT INTO city(name, state,latitude,longitude) VALUES('{name}','{state}',{latitude},{longitude});"
        )
        session.commit()
        
    print("City data inserted succcessfully.......")
    print(session.execute("SELECT * from city;").fetchall())
    
    #Insert initial data for weather
    city = session.execute("SELECT id from city where name = 'TORONTO'").fetchone()
    weather_data_queries = [
        ('2022-10-27',datetime.strptime('2022-10-27T00:00', '%Y-%m-%dT%H:%M'),20),
        ('2022-10-27',datetime.strptime('2022-10-27T12:00', '%Y-%m-%dT%H:%M'),10),
        ('2022-10-26',datetime.strptime('2022-10-26T00:00', '%Y-%m-%dT%H:%M'),-2),
        ('2022-10-26',datetime.strptime('2022-10-26T12:00', '%Y-%m-%dT%H:%M'),15),
        ('2022-10-25',datetime.strptime('2022-10-25T00:00', '%Y-%m-%dT%H:%M'),0),
        ('2022-10-25',datetime.strptime('2022-10-25T12:00', '%Y-%m-%dT%H:%M'),6),
        ('2022-10-24',datetime.strptime('2022-10-24T00:00', '%Y-%m-%dT%H:%M'),14),
        ('2022-10-24',datetime.strptime('2022-10-24T12:00', '%Y-%m-%dT%H:%M'),3),
        ('2022-10-23',datetime.strptime('2022-10-23T00:00', '%Y-%m-%dT%H:%M'),18),
        ('2022-10-23',datetime.strptime('2022-10-23T12:00', '%Y-%m-%dT%H:%M'),8),
        ('2022-10-22',datetime.strptime('2022-10-22T00:00', '%Y-%m-%dT%H:%M'),15),
        ('2022-10-22',datetime.strptime('2022-10-22T12:00', '%Y-%m-%dT%H:%M'),-1),
        ('2022-10-21',datetime.strptime('2022-10-21T00:00', '%Y-%m-%dT%H:%M'),12),
        ('2022-10-21',datetime.strptime('2022-10-21T12:00', '%Y-%m-%dT%H:%M'),10),
        ('2022-10-20',datetime.strptime('2022-10-20T00:00', '%Y-%m-%dT%H:%M'),14),
        ('2022-10-20',datetime.strptime('2022-10-20T12:00', '%Y-%m-%dT%H:%M'),8),
    ]
    for weather_data in weather_data_queries:
        session.execute(
            f""" INSERT INTO weather(date,recorded_datetime,temperature,weather_code,feels_like,dew_point,relative_humidity,pressure_value,pressure_trend,visibility,ceiling,wind_direction,wind_speed,wind_gust,city_id)
            VALUES ('{weather_data[0]}','{weather_data[1]}',{weather_data[2]},0,0,0,0,0,0,0,0,'N',0,0,{city[0]})
            """
        )
        session.commit()
    print("Weather data inserted succcessfully.......")
    print(session.execute("SELECT * from weather;").fetchall())
    

if __name__ == '__main__':
    seed_data()