import abc


class CarElementVisitor(abc.ABC):

    @abc.abstractmethod
    def visit_wheel(self, wheel):
        pass

    @abc.abstractmethod
    def visit_engine(self, engine):
        pass

    @abc.abstractmethod
    def visit_body(self, body):
        pass

    @abc.abstractmethod
    def visit_car(self, car):
        pass


class DoVisitor(CarElementVisitor):

    def visit_wheel(self, wheel):
        return 'Kicking my {} wheel'.format(wheel.name)

    def visit_engine(self, engine):
        return 'Starting my engine'

    def visit_body(self, body):
        return 'Moving my body'

    def visit_car(self, car):
        return 'Starting my car'


class PrintVisitor(CarElementVisitor):

    def visit_wheel(self, wheel):
        return 'Visiting {} wheel'.format(wheel.name)

    def visit_engine(self, engine):
        return 'Visiting engine'

    def visit_body(self, body):
        return 'Visiting body'

    def visit_car(self, car):
        return 'Visiting car'
