#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.sql.expression import column
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), ForeignKey("state.id"), nullable=False)
    name = column(String(128), nullable=False)
    __tablename__ = "cities"
    places = relationship("Place", backref="City")
