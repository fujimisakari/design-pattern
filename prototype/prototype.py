import abc
import copy


class Prototype(abc.ABC):

    @abc.abstractmethod
    def create_clone(self):
        pass


class ConcretePrototype(Prototype):

    def __init__(self, type_id):
        self.type_id = type_id

    def create_clone(self):
        return copy.copy(self)

    def get_type_id(self):
        return self.type_id
