#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column((Integer), default=0, nullable=False)
    number_bathrooms = Column((Integer), default=0, nullable=False)
    max_guest = Column((Integer), default=0, nullable=False)
    price_by_night = Column((Integer), default=0, nullable=False)
    latitude = Column((Float), nullable=True)
    longitude = Column((Float), nullable=True)
    reviews = relationship("Review", backref="place")

    @property
    def reviews(self):
        """Get a list of all linked Reviews"""
        review_list = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Get/set linked Amenities."""
        amenity_list = []
        for amenity in list(models.storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
