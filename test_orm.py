# !/usr/bin/env python
# -*- coding: utf8 -*-
import logging

from orm import Pdb
import json
import datetime

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# test
if __name__ == "__main__":
    # param = {"userId": 1, "address": "阿斯顿发送到发", "selected": 1}
    # Pdb.address.add_addresses(param)
    #
    # book = Pdb.book.get_book_by_id(3)
    # print(f"book == {book}")
    #
    # books = Pdb.book.get_all_books()
    # print(f"books == {books}")
    # param = {"name": "book3", "price": "24.00", 'author': 'Navy'}
    # Pdb.book.add_books(param)
    #
    # book = Pdb.book.search_books({'price': '24.00'})
    # print(book)
    #
    # Pdb.book.update_books({'name': 'book3'}, {"price": "9.01", "author": "author112"})
    # book = Pdb.book.search_books({"price": "9.01"})
    # print(f"the new book == {book}")
    #

    # param = {'email': '587978@qq.com', 'mobileNumber': '13936383200', 'isAdmin': 0, 'username': 'user6',
    #          'password': '623456'}
    # Pdb.user.add_users(param)
    #
    # Pdb.user.update_users({'username': 'user6'}, {'isActive': 1, 'isAdmin': 1})
    #
    # user = Pdb.user.search_users({'isAdmin': 1})
    # print(f'new_user == {user}')

    # param1 = {"userId": 2, "address": "北京市朝阳区", "selected": 0}
    # param2 = {"userId": 4, "address": "北京市海淀区", "selected": 1}
    # Pdb.address.add_addresses(param1)
    # Pdb.address.add_addresses(param2)
    # Pdb.address.update_addresses({'userId': 1}, {'address': '上海市徐汇区'})
    # Pdb.address.del_addresses({'userId': 4})
    #
    # address = Pdb.address.search_addresses({'selected': 1})
    # print(f'new == {address}')

    # param1 = {'name': '北京', 'isVisible': 1}
    # param2 = {'name': '上海', 'isVisible': 0}
    # Pdb.city.add_city(param1)
    # Pdb.city.add_city(param2)

    # Pdb.city.update_city({'id': 1}, {'isVisible': 1})
    # Pdb.city.add_city({'id': 174, 'name': '山河'})
    # city = Pdb.city.search_city({'id': 174})
    # print(city)
    #
    # Pdb.order.add_orders({'userId': 1, 'removed': 0})
    # Pdb.order.add_orders({'userId': 2, 'removed': 0})
    # Pdb.order.add_orders({'userId': 4, 'removed': 0})
    #
    # Pdb.order.update_orders({'userId': 4}, {'removed': 1})
    # orders = Pdb.order.search_orders({'removed': 1})
    # print(orders)
    # Pdb.order.del_orders({'id': 3})
    # Pdb.book_type.add_types({'name': '教材'})
    # Pdb.book_type.add_types({'name': '科幻'})
    # Pdb.book_type.add_types({'name': '语言'})
    # types = Pdb.book_type.get_all_types()
    # print(types)

    # Pdb.book_type.update_types({'id': 1},{'name': '课本'})
    # type = Pdb.book_type.search_types({'name': '课本'})
    # print(type)
    #
    # Pdb.book_type.del_types({'id': 1})
    #
    # book = Pdb.book.get_book_by_id(1)
    # print(json.dumps(book, cls=DateEncoder))

    user = Pdb.user.get_all_mobile_number()
    print(user)
