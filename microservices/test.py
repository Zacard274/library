import time

import requests
from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://admin:123123@localhost"}


# 同步方式
def compute():
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning the compute task
        msg_list = []
        for i in range(1000):
            msg = rpc.compute.compute("sum", i, 1)
            msg_list.append(msg)
        return msg_list


def compute_async():
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning the compute task
        msg_list = []
        for i in range(100):
            msg = rpc.compute.compute.call_async("sum", i, 1)
            msg_list.append(msg.result())
        return msg_list


def test_event():
    with ClusterRpcProxy(CONFIG) as rpc:
        # asynchronously spawning the compute task
        for i in range(100):
            rpc.service_a.dispatching_method.call_async("payload test")


def test_http():
    res = requests.get("http://localhost:8080/get/42")
    print(res.json())


if __name__ == "__main__":
    # start0 = time.time()
    # result1 = compute()
    # stop0 = time.time()
    # print(f"stop0-start0 == {stop0-start0} ")
    # start1 = time.time()
    # result2 = compute_async()
    # stop1 = time.time()
    # print(f"stop1-start1 == {stop1-start1}")
    # start2 = time.time()
    # test_event()
    # stop2 = time.time()
    # print(f"stop2-start2 == {stop2-start2}")
    test_http()
