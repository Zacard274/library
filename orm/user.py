# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from .base import base


class UserModel(base):
    __tablename__ = "user"

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    email = Column(VARCHAR(255), unique=True)
    mobileNumber = Column(VARCHAR(16))
    isActive = Column(BOOLEAN)
    isAdmin = Column(BOOLEAN)
    password = Column(VARCHAR(255))
    username = Column(VARCHAR(255), unique=True)
    receiveNoticeEmail = Column(BOOLEAN)
    passwordRecoveryCode = Column(VARCHAR(255))
    orderCount = Column(BIGINT(20))
    city_id = Column(BIGINT(20), ForeignKey("city.id"))
    successOrderCount = Column(BIGINT(20))
    realName = Column(VARCHAR(255))
    removed = Column(BOOLEAN)
