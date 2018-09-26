# !/usr/bin/env python
# -*- coding: utf8 -*-
import logging

from orm import Pdb

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)

# test
if __name__ == "__main__":
    # param = {"name": "python note book", "price": "11.24"}
    # Pdb.book.add_books(param)
    book = Pdb.book.get_book_by_id(3)
    print(f"book == {book}")

    books = Pdb.book.get_all_books()
    print(f"books == {books}")
