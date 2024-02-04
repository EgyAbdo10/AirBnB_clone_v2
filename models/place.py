#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship("Review", back_populates="place", cascade="all,delete")
        amenity_ids = []

else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        @property
        def reviews(self):
            from models.__init__ import storage
            from models.review import Review
            objs = storage.all(Review)
            obj_list = []
            for obj in objs.values:
                if obj.place_id == self.id:
                    obj_list.append(obj)
            return obj_list
