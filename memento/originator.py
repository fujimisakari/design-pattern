from .memento import Memento


class Originator():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def calc_add(self, add_num):
        self.param1 += add_num

    def concat(self, add_str):
        self.param2 = self.param2 + add_str

    def create_memento(self):
        return Memento(self.param1, self.param2)

    def set_memento(self, memento):
        self.param1 = memento.param1
        self.param2 = memento.param2

    def output(self):
        return 'param1=>{} / param2=>{}'.format(self.param1, self.param2)
