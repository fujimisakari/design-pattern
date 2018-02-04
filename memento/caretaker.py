from .originator import Originator


class Caretaker():

    def __init__(self):
        self.memento_list = []

    def main(self):
        originator = Originator(0, '')

        for i in range(5):
            for j in range(5):
                if j < i:
                    originator.calc_add(j)
                    originator.concat(str(j))
            self.memento_list.append(originator.create_memento())

        originator.calc_add(5)
        originator.concat('5')
        print(originator.output())

        while self.memento_list:
            memento = self.memento_list.pop()
            originator.set_memento(memento)
            print(originator.output())
