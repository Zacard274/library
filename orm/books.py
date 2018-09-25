# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, ForeignKey, BIGINT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship

from .base import base


class BooksModel(base):
    __tablename__ = 'books'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(VARCHAR(16))
    typeId = Column(BIGINT(20), ForeignKey("book_type.id"))
    bookType = relationship("BookTypeModel", back_populates="books")
    author = Column(VARCHAR(256))
    press = Column(VARCHAR(255))
    number = Column(INTEGER)
    orderId = Column(BIGINT(20), ForeignKey("order.id"))
    order = relationship("OrderModel", back_populates="books")
