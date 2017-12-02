import abc


class DisplayInterface(abc.ABC):

    @abc.abstractmethod
    def get_display_message(self):
        pass

    @abc.abstractmethod
    def display(self):
        pass
