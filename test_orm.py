# !/usr/bin/env python
# -*- coding: utf8 -*-
import logging

from orm import Pdb

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# test
if __name__ == "__main__":
    param = {"name": "python note book", "price": "11.24"}
    Pdb.book.add_books(param)
