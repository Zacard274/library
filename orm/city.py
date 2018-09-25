# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, VARCHAR, BIGINT, Boolean, INTEGER
from sqlalchemy.dialects.mysql import DOUBLE

from .base import base


class CityModel(base):
    __tablename__ = 'city'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    isVisible = Column(Boolean)
    latitude = Column(DOUBLE)
    longitude = Column(DOUBLE)
    name = VARCHAR(255)
    northEastLatitude = Column(DOUBLE)
    northEastLongitude = Column(DOUBLE)
    southWestLatitude = Column(DOUBLE)
    southWestLongitude = Column(DOUBLE)
    url = Column(VARCHAR(255))
    denyOrder = Column(Boolean)
    areaCode = Column(VARCHAR(255))
    localNumberLength = Column(INTEGER)
    extensionNumberPrefix = Column(VARCHAR(255))
    isInBadWeather = Column(Boolean)


class CityOrm(object):
    def __init__(self, db):
        self.db = db
