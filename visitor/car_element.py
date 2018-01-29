import abc


class CarElement(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor):
        pass


class Wheel(CarElement):

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_wheel(self)


class Engine(CarElement):

    def accept(self, visitor):
        visitor.visit_engine(self)


class Body(CarElement):

    def accept(self, visitor):
        visitor.visit_body(self)


class Car(CarElement):

    def __init__(self):
        self.elements = [
            Wheel('front left'), Wheel('front right'),
            Wheel('back left'), Wheel('back right'),
            Body(), Engine(),
        ]

    def accept(self, visitor):
        for elem in self.elements:
            elem.accept(visitor)
        visitor.visit_car(self)
