from sqlalchemy import Column,Integer,String,Float,UniqueConstraint
from sqlalchemy.orm import relationship

from sql_db import Base,session

class City(Base):
    __tablename__ = 'city'

    id = Column(
        Integer, 
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(200),
        nullable=False,
        doc='name of city'
    )
    
    state = Column(
        String(200),
        nullable=False,
        doc='state or province of city'
    )

    latitude = Column(
        Float,
        nullable=False,
        doc='latitude of city'
    )

    longitude = Column(
        Float,
        nullable=False,
        doc='longitude of city'
    )

    __table_args__ = (
        UniqueConstraint('name', 'state', name='unique_city_full_address'),
    )
    
    weather_data = relationship('Weather', back_populates='city_info')
    
    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, state={self.state}, latitude={self.latitude}, longitude={self.longitude}>"