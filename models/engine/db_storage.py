#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """class  dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == ('test'):
            meta = MetaData()
            Base.meta.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """query on the current database session
        (self.__session) all objects depending of the class name
        if cls=None, query all types of objects
        """
        if cls is not None and type(cls) == str:
            objects = self.__session.query(cls).all()
            for obj in objects:
                return "{}.{}".format(obj.__name__, obj.id)
        else:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """"""
        self.storage.close()
