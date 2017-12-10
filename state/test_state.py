import unittest

from .gumball_machine import GumballMachinea


class StateGumballMachineTest(unittest.TestCase):

    def setUp(self):
        self.gumball_machine = GumballMachinea(5)

    def test_state_insert_quarter(self):
        gumball_machine = GumballMachinea(5)
        result = gumball_machine.insert_quarter()
        self.assertEqual(result, '25セントを投入しました')

    def test_state_insert_quarter_fail(self):
        gumball_machine = GumballMachinea(5)
        result = gumball_machine.insert_quarter()
        result = gumball_machine.insert_quarter()
        self.assertEqual(result, 'もう一度25セントを投入することはできません')

    def test_state_eject_quarter(self):
        gumball_machine = GumballMachinea(5)
        gumball_machine.insert_quarter()
        result = gumball_machine.eject_quarter()
        self.assertEqual(result, '25セントを返却しました')

    def test_state_turn_crank_winner(self):
        gumball_machine = GumballMachinea(5)
        gumball_machine.insert_quarter()
        result = gumball_machine.turn_crank(True)
        self.assertEqual(result, 'クランクを回しました...')

    def test_state_dispense_success(self):
        gumball_machine = GumballMachinea(5)
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank(0)
        result = gumball_machine.dispense()
        self.assertEqual(result, '当たりです!25セントで2つのガムボールがもらえます')
        self.assertEqual(gumball_machine.count, 3)

    def test_state_dispense_failure(self):
        gumball_machine = GumballMachinea(5)
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank(1)
        result = gumball_machine.dispense()
        self.assertEqual(result, 'まだ、チャレンジできるよ')
        self.assertEqual(gumball_machine.count, 4)

    def test_state_sold_out(self):
        gumball_machine = GumballMachinea(1)
        gumball_machine.insert_quarter()
        gumball_machine.turn_crank(0)
        result = gumball_machine.dispense()
        self.assertEqual(result, 'おっと、ガムボールがなくなりました!')
        self.assertEqual(gumball_machine.count, 0)
