from .mediator import MediatorAbstract


class Mediator(MediatorAbstract):

    def __init__(self):
        self.colleagues = []

    def add_colleague(self, colleague):
        self.colleagues.append(colleague)

    def consultation(self, colleague):
        name = colleague.get_name()
        # print('{}からの相談です。'.format(name))

        for c in self.colleagues:
            if c.get_name() != colleague.get_name():
                return c.advice('{}からの相談がありましたよ。'.format(name))
