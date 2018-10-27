from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://admin:123123@localhost"}


def func():
    with ClusterRpcProxy(config=CONFIG) as rpc:
        res = rpc.first.hello.call_async('Tom')
        return res.result()


if __name__ == '__main__':
    func()