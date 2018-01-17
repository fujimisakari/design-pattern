import unittest

from .colleague_a import ColleagueA
from .colleague_b import ColleagueB
from .mediator_concrete import Mediator


class MediatorTest(unittest.TestCase):

    def setUp(self):
        mediator = Mediator()
        col_a = ColleagueA('A')
        col_b = ColleagueB('B')
        mediator.add_colleague(col_a)
        mediator.add_colleague(col_b)
        col_a.set_mediator(mediator)
        col_b.set_mediator(mediator)
        self.col_a = col_a
        self.col_b = col_b

    def test_colleague_a(self):
        msg = self.col_a.run()
        self.assertEqual(msg, 'ConcreteColleagueB: Aからの相談がありましたよ。')

    def test_colleague_b(self):
        msg = self.col_b.run()
        self.assertEqual(msg, 'ConcreteColleagueA: Bからの相談がありましたよ。')
