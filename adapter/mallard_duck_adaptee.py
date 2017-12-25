from .duck_interface import DuckInterface


class MallardDuckAdaptee(DuckInterface):

    def quack(self):
        return 'Quack'

    def fly(self):
        return 'Im flying'
