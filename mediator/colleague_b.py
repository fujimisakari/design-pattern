from .colleague import ColleagueAbstract


class ColleagueB(ColleagueAbstract):

    def __init__(self, name):
        super(ColleagueB, self).__init__(name)

    def advice(self, msg):
        return 'ConcreteColleagueB: {}'.format(msg)

    def run(self):
        return self.mediator.consultation(self)
