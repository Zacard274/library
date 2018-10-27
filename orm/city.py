# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, VARCHAR, BIGINT, Boolean, INTEGER
from sqlalchemy.dialects.mysql import DOUBLE

from .base import MyMixin, Base, BaseOrm
from utils.orm_format import model_to_list, session_auto_commit


class CityModel(Base):
    __tablename__ = 'city'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    isVisible = Column(Boolean)
    latitude = Column(DOUBLE)
    longitude = Column(DOUBLE)
    name = Column(VARCHAR(255))
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


class CityOrm(BaseOrm):
    def __init__(self, db):
        super().__init__(db)

    @model_to_list
    def gel_all_city(self):
        return self.session.query(CityModel).order_by(CityModel.id).all()

    @session_auto_commit
    def add_city(self, param):
        new_city = CityModel(**param)
        self.session.add(new_city)

    @session_auto_commit
    def del_city_by_id(self, city_id):
        del_city = self.session.query(CityModel).filter_by(Id=city_id).first()
        self.session.delete(del_city)

    @model_to_list
    def search_city(self, param):
        return self.session.query(CityModel).filter_by(**param).all()

    @session_auto_commit
    def update_city(self, query_param, update_param):
        self.session.query(CityModel).filter_by(**query_param).update(update_param)
