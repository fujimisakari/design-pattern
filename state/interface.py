import abc


class GumballMachineStateInterface(abc.ABC):

    @abc.abstractmethod
    def insert_quarter(self):
        pass

    @abc.abstractmethod
    def eject_quarter(self):
        pass

    @abc.abstractmethod
    def turn_crank(self, force_winner):
        pass

    @abc.abstractmethod
    def dispense(self):
        pass
