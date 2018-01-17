import abc


class MediatorAbstract(abc.ABC):

    @abc.abstractmethod
    def add_colleague(self, colleague):
        pass

    @abc.abstractmethod
    def consultation(self, colleague):
        pass
