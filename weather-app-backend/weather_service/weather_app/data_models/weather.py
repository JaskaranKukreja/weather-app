from sqlalchemy import Column,Integer,String,Float,UniqueConstraint,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from sql_db import Base,session


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(
        Integer, 
        primary_key=True,
        autoincrement=True
    )

    date = Column(
        String(20),
        nullable=False,
        doc='date in format YYYY-MM-DD'
    )
    
    recorded_datetime = Column(
        DateTime,
        nullable=False,
        doc='utc time of the recorded weather'
    )
    
    weather_code = Column(
        String(2),
        nullable=False,
        doc='weather code of the recorded weather'
    )

    temperature = Column(
        Float,
        nullable=False,
        doc='temperature in celsius'
    )

    dew_point = Column(
        Float,
        nullable=False,
        doc='dew_point of the recorded weather'
    )

    feels_like = Column(
        Float,
        nullable=False,
        doc='feels_like temperature in celsius'
    )
    
    relative_humidity = Column(
        Float,
        nullable=False,
        doc='relative_humidity of the recorded weather'
    )
    
    pressure_value = Column(
        Float,
        nullable=False,
        doc='pressure_value of the recorded weather'
    )
    
    pressure_trend = Column(
        Float,
        nullable=False,
        doc='pressure_trend of the recorded weather'
    )   
    
    visibility = Column(
        Float,
        nullable=False,
        doc='visibility of the recorded weather'
    )
    
    ceiling = Column(
        Float,
        nullable=False,
        doc='ceiling of the recorded weather'
    )
    
    wind_direction = Column(
        String(2),
        nullable=False,
        doc='wind_direction of the recorded weather'
    )
    
    wind_speed = Column(
        Float,
        nullable=False,
        doc='wind_speed of the recorded weather'
    )
    
    wind_gust = Column(
        Float,
        nullable=False,
        doc='wind_gust of the recorded weather'
    )
    city_id = Column(
        Integer(),
        ForeignKey("city.id"),
        nullable=False,
    )
    
    city_info = relationship('City', back_populates='weather_data')
    
    def __repr__(self):
        return f"<Weather(id={self.id},city={self.city_info},temperature={self.temperature},date={self.date},recorded_datetime={self.recorded_datetime},weather_code={self.weather_code})>"