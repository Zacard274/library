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
            return [_model2dict(ret)] if _model2dict(ret) else []

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
        if not key.startswith("_") and key != "metadata" and not hasattr(getattr(obj, key), "__tablename__"):
            obj_dict[key] = getattr(obj, key)
    return obj_dict


def session_auto_commit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        ret = func(*args, **kw)
        obj = args[0]
        try:
            obj.session.commit()
        except Exception as e:
            raise e
        finally:
            obj.session.close()
        return ret

    return wrapper
