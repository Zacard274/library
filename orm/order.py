# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from .base import base, NotNullColumn


class OrderModel(base):
    __tablename__ = 'order'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    sum = Column(VARCHAR(16))
    orderStatus = Column(TINYINT(3))
    orderType = Column(TINYINT(3))
    removed = Column(BOOLEAN)
    books = relationship("BooksModel", back_populates="order")
    userId = NotNullColumn(BIGINT, ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="orders")


class OrderOrm(object):
    def __init__(self, db):
        self.db = db
