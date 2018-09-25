# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, VARCHAR, BIGINT
from sqlalchemy.orm import relationship

from .base import base


class BookTypeModel(base):
    __tablename__ = 'book_type'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    books = relationship("BooksModel", back_populates="bookType")


class BookTypeOrm(object):
    def __init__(self, db):
        self.db = db
