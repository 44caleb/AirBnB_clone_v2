#!/usr/bin/python3
""" creates the database storage engine """


import os
from sqlalchemy import create_engine


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