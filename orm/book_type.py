# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, VARCHAR, BIGINT
from sqlalchemy.orm import relationship

from .base import MyMixin, Base
from utils.orm_format import model_to_list, session_auto_commit


class BookTypeModel(MyMixin, Base):
    __tablename__ = 'book_type'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    books = relationship("BooksModel", back_populates="bookType")


class BookTypeOrm(object):
    def __init__(self, db):
        self.session = db.get_session()

    @model_to_list
    def get_all_types(self):
        return self.session.query(BookTypeModel).order_by(BookTypeModel.id).all()

    @session_auto_commit
    def add_types(self, param):
        new_type = BookTypeModel(**param)
        self.session.add(new_type)

    @session_auto_commit
    def del_types(self, param):
        del_types = self.session.query(BookTypeModel).filter_by(**param).first()
        self.session.delete(del_types)

    @model_to_list
    def search_types(self, param):
        types = self.session.query(BookTypeModel).filter_by(**param).all()
        return types

    @session_auto_commit
    def update_types(self, query_param, update_param):
        self.session.query(BookTypeModel).filter_by(**query_param).update(update_param)
