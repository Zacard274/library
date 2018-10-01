# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, ForeignKey, BIGINT, VARCHAR, INTEGER, or_
from sqlalchemy.orm import relationship

from .base import Base, MyMixin, BaseOrm
from utils.orm_format import model_to_list, model_to_dict, session_auto_commit


class BooksModel(MyMixin, Base):
    __tablename__ = 'books'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(VARCHAR(16))
    typeId = Column(BIGINT, ForeignKey("book_type.id"))
    bookType = relationship("BookTypeModel", back_populates="books")  # lazy模式
    author = Column(VARCHAR(255))
    press = Column(VARCHAR(255))
    number = Column(INTEGER)
    orderId = Column(BIGINT, ForeignKey("order.id"))
    order = relationship("OrderModel", back_populates="books")


class BooksOrm(BaseOrm):
    def __init__(self, db):  # db是__init__.py中Orm的实例作为参数传进来
        super().__init__(db)

    @session_auto_commit
    def add_books(self, param):
        new_book = BooksModel(**param)
        self.session.add(new_book)

    @model_to_dict
    def get_book_by_id(self, book_id):
        return self.session.query(BooksModel).filter_by(id=book_id).first()

    @model_to_list
    def get_all_books(self):
        return self.session.query(BooksModel).order_by(BooksModel.id).all()

    @session_auto_commit
    def del_book_by_id(self, book_id):
        del_book = self.session.query(BooksModel).filter_by(id=book_id).first()
        self.session.delete(del_book)

    @session_auto_commit
    def update_books(self, query_param, update_param):
        self.session.query(BooksModel).filter_by(**query_param).update(update_param)

    @model_to_list
    def search_books(self, keyword, **kw):

        book = self.session.query(BooksModel)
        if keyword:
            # book = book.filter(text("name like :param OR author like :param")).params(param=f"%{keyword}%")
            book = book.filter(or_(BooksModel.name.like(f'%{keyword}%'), BooksModel.author.like(f'%{keyword}%')))
        if kw:
            book = book.filter_by(**kw)
        books = book.all()
        return books
