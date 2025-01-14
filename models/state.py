#!/usr/bin/python3
""" State Module for HBNB project """
from models.engine.file_storage import FileStorage
from models.city import City
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City",  backref="state")

    if models.storage == FileStorage():
        @property
        def cities(self):
            city_list = []
            for city in models.storage.all(City).values:
                if city.state_id == self.city.id:
                    city_list.append(city)
            return city_list
