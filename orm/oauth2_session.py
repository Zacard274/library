# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from .base import MyMixin, Base, BaseOrm
from utils.orm_format import model_to_dict


class Oauth2SessionModel(MyMixin, Base):
    __tablename__ = "oauth2session"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    accessToken = Column(VARCHAR(255))
    accessTokenExpireTime = Column(DATETIME)
    refreshToken = Column(VARCHAR(255))
    removed = Column(BOOLEAN)
    timestamp = Column(DATETIME)
    uniqueId = Column(VARCHAR(255))
    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="oauth2_session")


class Oauth2SessionOrm(BaseOrm):
    def __init__(self, db):
        super().__init__(db)

    @model_to_dict
    def get_user_by_access_token(self, access_token):
        oauth2_session = self.session.query(Oauth2SessionModel).filter_by(accessToken=access_token).first()

        user = oauth2_session.user
        return user
