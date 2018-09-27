# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from .base import NotNullColumn, MyMixin, Base
from utils.orm_format import session_auto_commit, model_to_list


class OrderModel(MyMixin, Base):
    __tablename__ = 'order'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    sum = Column(VARCHAR(16))
    orderStatus = Column(TINYINT(3))
    orderType = Column(TINYINT(3))
    removed = Column(BOOLEAN)
    books = relationship("BooksModel", back_populates="order")
    userId = NotNullColumn(BIGINT, ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="orders")


class OrderOrm(object):
    def __init__(self, db):
        self.session = db.get_session()

    @model_to_list
    def get_all_orders(self):
        return self.session.query(OrderModel).order_by(OrderModel.id).all()

    @session_auto_commit
    def add_orders(self, param):
        new_order = OrderModel(**param)
        self.session.add(new_order)

    @session_auto_commit
    def del_orders(self, param):
        del_order = self.session.query(OrderModel).filter_by(**param).first()
        self.session.delete(del_order)

    @model_to_list
    def search_orders(self, param):
        orders = self.session.query(OrderModel).filter_by(**param).all()
        return orders

    @session_auto_commit
    def update_orders(self, query_param, update_param):
        self.session.query(OrderModel).filter_by(**query_param).update(update_param)
