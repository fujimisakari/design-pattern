
class Sorter():

    def __init__(self, implementor):
        self.implementor = implementor

    def sort(self):
        return self.implementor.sort()
