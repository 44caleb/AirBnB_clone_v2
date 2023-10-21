#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from models.city import City
from sqlalchemy.orm import relationship
import models
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
    
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """retrieves all instances of cities for a given state object id"""
            related_cities = []

            for obj in models.storage.all().values():
                if isinstance(obj, City):
                    if obj.state_id == self.id:
                        related_cities.append(obj)
            return related_cities
