import abc

from ..beverage_abstract import BeverageAbstract


class CondimentDecorator(BeverageAbstract):

    # Beverage.get_descriptionがabstractになってないので再定義
    @abc.abstractmethod
    def get_description(self):
        pass
