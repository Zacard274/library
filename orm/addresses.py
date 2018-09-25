# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base import base


class AddressesModel(base):
    __tablename__ = 'addresses'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    userId = Column(BIGINT(20), ForeignKey('user.id'))
    user = relationship("UserModel", back_populates="addresses")
    address = Column(VARCHAR(255))
    selected = Column(BOOLEAN)
    removed = Column(BOOLEAN, default=0)