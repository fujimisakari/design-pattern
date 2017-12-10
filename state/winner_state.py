from .constants import GumballMachineStat
from .interface import GumballMachineStateInterface


class WinnerState(GumballMachineStateInterface):
    """
    当たりがあたった状態
    """
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        return 'お待ちください。すでにガムボールを出しています'

    def eject_quarter(self):
        return '申し分けありせん。すでにクランクを回しています'

    def turn_crank(self, force_winner):
        return '2回まわしてもガムボールをもう1つ手に入れることはできません'

    def dispense(self):
        self.gumball_machine.release_ball()

        if not self.gumball_machine.can_dispense:
            self.gumball_machine.set_state(GumballMachineStat.SOLD_OUT)
            return 'おっと、ガムボールがなくなりました!'

        self.gumball_machine.release_ball()

        if not self.gumball_machine.can_dispense:
            self.gumball_machine.set_state(GumballMachineStat.SOLD_OUT)
            return 'おっと、ガムボールがなくなりました!'

        self.gumball_machine.set_state(GumballMachineStat.NO_QUARTER)
        return '当たりです!25セントで2つのガムボールがもらえます'
