from .colleague import ColleagueAbstract


class ColleagueA(ColleagueAbstract):

    def __init__(self, name):
        super(ColleagueA, self).__init__(name)

    def advice(self, msg):
        return 'ConcreteColleagueA: {}'.format(msg)

    def run(self):
        return self.mediator.consultation(self)
