# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from .base import base

class OrderModel(base):
    __tablename__ = 'order'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    bookId = Column(BIGINT(20))
    sum = Column(VARCHAR(16))
    orderStatus = Column(TINYINT(3))
    ordertype = Column(TINYINT(3))
    removed = Column(BOOLEAN)
