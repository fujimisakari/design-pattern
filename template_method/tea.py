from .caffeine_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):

    def brew(self):
        return 'Steeping the tea'

    def add_condiments(self):
        return 'Adding Lemon'
