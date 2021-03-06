# !/usr/bin/env python
import json
import time

from nameko.events import EventDispatcher, event_handler
from nameko.rpc import rpc
from nameko.web.handlers import http

# 1.event
# 把payload分发的过程，分发给event_type，
class ServiceA:
    """ Event dispatching service. """
    name = "service_a"

    dispatch = EventDispatcher()

    @rpc
    def dispatching_method(self, payload):
        self.dispatch("event_type", payload)


# event_type的处理函数
class ServiceB:
    """ Event listening service. """
    name = "service_b"

    @event_handler("service_a", "event_type")
    def handle_event(self, payload):
        time.sleep(100)
        print("service b received:", payload)


# 2.rpc
class Compute(object):
    name = "compute"

    @rpc
    def compute(self, operation, value, other):
        operations = {'sum': lambda x, y: int(x) + int(y),
                      'mul': lambda x, y: int(x) * int(y),
                      'div': lambda x, y: int(x) / int(y),
                      'sub': lambda x, y: int(x) - int(y)}
        try:
            result = operations[operation](value, other)
        except Exception:
            raise
        else:
            return result


# 3.http
class HttpService:
    name = "http_service"

    # @http('方法', '/路由')
    @http('GET', '/get/<int:value>')
    def get_method(self, request, value):
        return json.dumps({'value': value})

    @http('POST', '/post')
    def do_post(self, request):
        return u"received: {}".format(request.get_data(as_text=True))

    @http('GET,PUT,POST,DELETE', '/multi')
    def do_multi(self, request):
        return request.method
