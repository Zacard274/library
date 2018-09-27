# !/usr/bin/env python
# -*- coding: utf8 -*-


from functools import partial

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATETIME, TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr, declarative_base

NotNullColumn = partial(Column, nullable=False, server_default="")


# class ModelBase(object):
class MyMixin(object):
    create_time = NotNullColumn(DATETIME)
    update_time = NotNullColumn(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")

    @declared_attr
    def __table_args__(cls):
        return {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8'
        }


# base = declarative_base(cls=ModelBase)

Base = declarative_base()


