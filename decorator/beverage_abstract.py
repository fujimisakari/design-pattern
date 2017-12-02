import abc


class BeverageAbstract(abc.ABC):
    description = '不明な飲み物'

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def cost(self):
        pass
