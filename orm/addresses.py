# !/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base, BaseOrm

from utils.orm_format import model_to_list, session_auto_commit


class AddressesModel(Base):
    __tablename__ = 'addresses'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    userId = Column(BIGINT, ForeignKey('user.id'), nullable=False)
    user = relationship("UserModel", back_populates="addresses")
    address = Column(VARCHAR(255))
    selected = Column(BOOLEAN)
    removed = Column(BOOLEAN, default=0)


class AddressesOrm(BaseOrm):
    def __init__(self, db):
        super().__init__(db)

    @model_to_list
    def get_all_addresses(self):
        return self.session.query(AddressesModel).order_by(AddressesModel.id).all()

    @session_auto_commit
    def add_addresses(self, param):
        new_addresses = AddressesModel(**param)
        self.session.add(new_addresses)

    @session_auto_commit
    def del_addresses(self, param):
        del_addresses = self.session.query(AddressesModel).filter_by(**param).first()
        self.session.delete(del_addresses)

    @model_to_list
    def search_addresses(self, param):
        addresses = self.session.query(AddressesModel).filter_by(**param).all()
        return addresses

    @session_auto_commit
    def update_addresses(self, query_param, update_param):
        self.session.query(AddressesModel).filter_by(**query_param).update(update_param)
