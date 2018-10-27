from nameko.rpc import rpc, RpcProxy


class Service2():
    name = 'second'

    @rpc
    def meet(self, content):
        return f'{content}, nice to meet you!'


# 调用second的方法，要用RpcProxy
class Service1():
    name = 'first'

    new = RpcProxy('second')

    @rpc
    def hello(self, name):
        res = f'hello {name}'
        return self.new.meet(res)

