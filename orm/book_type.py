# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, VARCHAR, Boolean, BIGINT, ForeignKey
from .base import base


class Book_typeModel(base):
    __tablename__ = 'book_type'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))


