# !/usr/bin/env python

import json
from datetime import datetime, date

from werkzeug.local import LocalStack, LocalProxy
from flask import request

from orm import Pdb

_user_stack = LocalStack()
# LocalStack 是用 Local 实现的栈结构，可以将对象推入、弹出，也可以快速拿到栈顶对象。

def get_current_user():
    top = _user_stack.top
    if top is None:
        raise RuntimeError()
    return top


current_user = LocalProxy(get_current_user)
#


def before_request():
    access_token = request.headers["Authorization"]
    user = Pdb.oauth2_session.get_user_by_access_token(access_token)
    if not user:
        print("user is None")
    _user_stack.push(user)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


_success = {
    "result_code": "ok",
    "result_code_desc": "success",
    "data": " "
}

_fail = {
    "result_code": "error",
    "result_code_desc": ""
}


def json_success(data):
    _success["data"] = data
    return json.dumps(_success, cls=ComplexEncoder)


def json_fail(desc):
    _fail["result_code_desc"] = desc
    return json.dumps(_fail, cls=ComplexEncoder)
