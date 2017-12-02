import abc


class ObserverInterface(abc.ABC):

    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
