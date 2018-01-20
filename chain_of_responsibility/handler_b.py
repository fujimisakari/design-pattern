from .handler import HandlerAbstract


class HandlerB(HandlerAbstract):

    def __init__(self, name):
        super(HandlerB, self).__init__(name)

    def request(self, req):
        if req % 2 == 0:
            return '{}：ようこそ!偶数は私のテリトリーです。'.format(self.name)
        elif self.next:
            return self.next.request(req)
        return '{}：無念!偶数以外は・・・!次もいないー'.format(self.name)
