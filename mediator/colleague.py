import abc


class ColleagueAbstract(abc.ABC):

    def __init__(self, name):
        self.name = name
        self.mediator = None

    def get_name(self):
        return self.name

    def set_mediator(self, mediator):
        self.mediator = mediator

    @abc.abstractmethod
    def advice(self, msg):
        pass

    @abc.abstractmethod
    def run(self):
        pass
