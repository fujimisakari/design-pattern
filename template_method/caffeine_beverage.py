import abc


class CaffeineBeverage(abc.ABC):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abc.abstractmethod
    def brew(self):
        pass

    @abc.abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        return 'Boiling water'

    def pour_in_cup(self):
        return 'Pouring into cup'
