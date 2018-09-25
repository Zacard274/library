#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .addresses import AddressesOrm
from .book_type import BookTypeOrm
from .books import BooksOrm
from .city import CityOrm
from .order import OrderOrm
from .user import UserOrm


class Orm(object):
    def __init__(self):
        self.username = os.environ.get("MYSQL_USERNAME")
        self.password = os.environ.get("MYSQL_PASSWORD")
        self.database = os.environ.get("MYSQL_DATABASE")
        print(f"{self.username }, {self.password }")
        self.__session_init()
        self.user = UserOrm(self)
        self.order = OrderOrm(self)
        self.city = CityOrm(self)
        self.book = BooksOrm(self)
        self.book_type = BookTypeOrm(self)
        self.address = AddressesOrm(self)

    def __engine(self):
        engine = create_engine(f"mysql+pymysql://{self.username}:{self.password}@127.0.0.1:3306/{self.database}")
        return engine

    def __session_init(self):
        self.session = scoped_session(sessionmaker(bind=self.__engine()))()

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.__engine()

    def get_connection(self):
        # if you want use transaction
        return self.__engine().connect()


Pdb = Orm()
