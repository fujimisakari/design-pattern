import abc


class HandlerAbstract(abc.ABC):

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next
        return next

    @abc.abstractmethod
    def request(self, req):
        pass
