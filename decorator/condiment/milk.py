from .decorator import CondimentDecorator


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 30

    def get_description(self):
        return self.beverage.get_description() + '、ミルク入り'
