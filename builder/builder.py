import abc


class Builder(abc.ABC):

    @abc.abstractmethod
    def build_base(self):
        pass

    @abc.abstractmethod
    def build_frame(self):
        pass

    @abc.abstractmethod
    def build_wall(self):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass
