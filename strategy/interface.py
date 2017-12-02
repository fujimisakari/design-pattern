import abc


class QuackBehaviorInterface(abc.ABC):

    @abc.abstractmethod
    def quack(self):
        pass
