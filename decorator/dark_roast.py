from .beverage_abstract import BeverageAbstract


class DarkRoast(BeverageAbstract):

    def __init__(self):
        self.description = 'ダークロースト'

    def cost(self):
        return 340
