# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, ForeignKey, Boolean, BIGINT, VARCHAR
from .base import base

class BooksModel(base):
    __tablename__ = 'books'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(VARCHAR(16))
    type_id = Column(BIGINT(20), ForeignKey("book_type.id"))
    author = Column(VARCHAR(256))
    press = Column(VARCHAR(255))
    number = Column(int)