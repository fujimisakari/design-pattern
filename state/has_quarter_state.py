import random

from .constants import GumballMachineStat
from .interface import GumballMachineStateInterface


class HasQuarterState(GumballMachineStateInterface):
    """
    お金を投入した状態
    """
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return 'もう一度25セントを投入することはできません'

    def eject_quarter(self):
        self.gumball_machine.set_state(GumballMachineStat.NO_QUARTER)
        return '25セントを返却しました'

    def turn_crank(self, force_winner):
        winner = random.randint(0, 11)
        if force_winner is not None:
            winner = force_winner

        if winner == 0 and self.gumball_machine.count > 1:
            self.gumball_machine.set_state(GumballMachineStat.WINNER)
        else:
            self.gumball_machine.set_state(GumballMachineStat.SOLD)
        return 'クランクを回しました...'

    def dispense(self):
        return '販売するガムボールはありません'
