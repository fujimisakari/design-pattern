from .caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):

    def brew(self):
        return 'Dripping Coffee through filter'

    def add_condiments(self):
        return 'Adding Sugar and Milk'
