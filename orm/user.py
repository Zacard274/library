# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base import base


class UserModel(base):
    __tablename__ = "user"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(255), unique=True)
    mobileNumber = Column(VARCHAR(16))
    isActive = Column(BOOLEAN)
    isAdmin = Column(BOOLEAN)
    password = Column(VARCHAR(255))
    username = Column(VARCHAR(255), unique=True)
    receiveNoticeEmail = Column(BOOLEAN)
    passwordRecoveryCode = Column(VARCHAR(255))
    orderCount = Column(BIGINT)
    city_id = Column(BIGINT, ForeignKey("city.id"))
    successOrderCount = Column(BIGINT)
    realName = Column(VARCHAR(255))
    removed = Column(BOOLEAN)
    orders = relationship("OrderModel", back_populates="user")
    addresses = relationship("AddressesModel", back_populates="user")


class UserOrm(object):
    def __init__(self, db):
        self.db = db
