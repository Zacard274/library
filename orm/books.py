# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, ForeignKey, BIGINT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship

from .base import base
from utils.orm_format import model_to_list, model_to_dict


class BooksModel(base):
    __tablename__ = 'books'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(VARCHAR(16))
    typeId = Column(BIGINT, ForeignKey("book_type.id"))
    bookType = relationship("BookTypeModel", back_populates="books")
    author = Column(VARCHAR(256))
    press = Column(VARCHAR(255))
    number = Column(INTEGER)
    orderId = Column(BIGINT, ForeignKey("order.id"))
    order = relationship("OrderModel", back_populates="books")


class BooksOrm(object):
    def __init__(self, db):
        self.session = db.get_session()

    def add_books(self, param):
        new_book = BooksModel(**param)
        self.session.add(new_book)
        self.session.commit()
        self.session.close()

    @model_to_dict
    def get_book_by_id(self, id):
        return self.session.query(BooksModel).filter_by(id=id).first()

    @model_to_list
    def get_all_books(self):
        return self.session.query(BooksModel).order_by(BooksModel.id).all()
