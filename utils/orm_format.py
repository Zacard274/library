# !/user/bin/env python
# -*- coding: utf8 -*-

from functools import wraps


def model_to_list(func):
    @wraps(func)
    def wrapper(*arg, **kw):
        ret = func(*arg, **kw)
        if isinstance(ret, list):
            return [_model2dict(obj) for obj in ret]
        else:
            return [_model2dict(ret)]

    return wrapper


def model_to_dict(func):
    @wraps(func)
    def wrapper(*arg, **kw):
        ret = func(*arg, **kw)
        if isinstance(ret, list):
            raise AttributeError
        else:
            return _model2dict(ret)

    return wrapper


def _model2dict(obj):
    obj_dict = dict()
    for key in dir(obj):
        if not key.startswith("_") and key != "metadata":
            obj_dict[key] = getattr(obj, key)
    return obj_dict