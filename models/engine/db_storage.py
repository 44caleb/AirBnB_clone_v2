#!/usr/bin/python3
""" creates the database storage engine """


import os
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """creates the class for the database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the database storage object"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        db_url = "{}+{}://{}:{}@{}/{}".format(dialect, driver, user, pwd, host, database)

        # creating the engine
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """queries database to retrieve all objs or objs of a class"""
        dictionary = {}
        if cls != None:
            objs = self.__session.query((cls)).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dictionary[key] = obj
        else:
            for subclass in Base.__subclasses__():
                objs = self.__session.query(subclass).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dictionary[key] = obj
        return dictionary
        
    def new(self, obj):
        """adds object to the current db session"""
        if obj:
            try:
                self.__session.add(obj)
            except:
                pass

    def save(self):
        """ commits changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current db session"""
        if obj is not None:
            self.__session.delete(obj)
        
    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """closes the db session"""
        self.__session.close()
