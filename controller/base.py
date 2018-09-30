# !/usr/bin/env python

import json
from datetime import datetime, date


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