from .handler import HandlerAbstract


class HandlerA(HandlerAbstract):

    def __init__(self, name, range_s, range_e):
        super(HandlerA, self).__init__(name)
        self.range_s = range_s
        self.range_e = range_e

    def request(self, req):
        if req >= self.range_s and req <= self.range_e:
            return '{}：私が成敗してくれるわ!'.format(self.name)
        elif self.next:
            return self.next.request(req)
        return '{}：次の者がおりませぬー'.format(self.name)
