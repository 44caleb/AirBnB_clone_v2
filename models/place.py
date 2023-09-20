#!/usr/bin/python3
""" Place Module for HBNB project """


import os
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', cascade='all, delete-orphan',
                           backref='place')
    amenities = relationship('Amenity',
                             secondary=place_amenity,
                             back_populates="place_amenities", viewonly=False)
    amenity_ids = []

    if os.getenv("HBNB_MYSQL_DB") != "db":
        @property
        def reviews(self):
            """ returns review objects associated with place id"""
            result = []
            rev_objs = models.storage.all('Review').values()
            for obj in rev_objs:
                if obj.place_id == self.id:
                    result.append(obj)
            return result

        @property
        def amenities(self):
            """gets list of amenity instances"""
            all_amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    all_amenities.append(amenity)
            return all_amenities

        @amenities.setter
        def amenities(self, obj):
            """
            sets amenity instances in list
            """
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
