# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy.dialects.mysql import DOUBLE, TINYINT
from sqlalchemy import Column, VARCHAR, ForeignKey, BIGINT, Boolean

class CityModel(base):
    __tablename__ = 'city'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
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
    localNumberLength = Column(int(11))
    meicanExtensionNumberPrefix = Column(VARCHAR(255))
    isInBadWeather = Column(Boolean)