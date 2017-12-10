from .constants import GumballMachineStat
from .interface import GumballMachineStateInterface


class NoQuarterState(GumballMachineStateInterface):
    """
    まだお金を入れてない状態
    """

    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        self.gumball_machine.set_state(GumballMachineStat.HAS_QUARTER)
        return '25セントを投入しました'

    def eject_quarter(self):
        return '25セントを投入していません'

    def turn_crank(self, force_winner):
        return 'クランクを回しましたが、25セントを投入していません'

    def dispense(self):
        return 'まず支払いをする必要があります'
