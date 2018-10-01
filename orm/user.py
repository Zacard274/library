# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base import MyMixin, Base, BaseOrm

from utils.orm_format import model_to_list, session_auto_commit


class UserModel(MyMixin, Base):
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
    oauth2_session = relationship("Oauth2SessionModel", back_populates="user")


class UserOrm(BaseOrm):
    def __init__(self, db):
        super().__init__(db)

    @model_to_list
    def get_all_users(self):
        return self.session.query(UserModel).order_by(UserModel.id).all()

    def get_all_mobile_number(self):
        return self.session.query(UserModel.mobileNumber).all()

    @session_auto_commit
    def add_users(self, param):
        new_user = UserModel(**param)
        self.session.add(new_user)

    @session_auto_commit
    def del_users(self, param):
        del_user = self.session.query(UserModel).filter_by(**param).first()
        self.session.delete(del_user)

    @model_to_list
    def search_users(self, param):
        users = self.session.query(UserModel).filter_by(**param).first()
        return users

    @session_auto_commit
    def update_users(self, query_param, update_param):
        self.session.query(UserModel).filter_by(**query_param).update(update_param)
