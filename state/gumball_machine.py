from .constants import GumballMachineStat
from .has_quarter_state import HasQuarterState
from .no_quarter_state import NoQuarterState
from .sold_out_state import SoldOutState
from .sold_state import SoldState
from .winner_state import WinnerState


class GumballMachinea():

    def __init__(self, number_gameball):
        sold_out_state = SoldOutState(self)
        no_quarter_state = NoQuarterState(self)

        self.count = number_gameball
        self.current_state = sold_out_state

        self.state_map = {
            GumballMachineStat.HAS_QUARTER: HasQuarterState(self),
            GumballMachineStat.SOLD: SoldState(self),
            GumballMachineStat.SOLD_OUT: sold_out_state,
            GumballMachineStat.NO_QUARTER: no_quarter_state,
            GumballMachineStat.WINNER: WinnerState(self),
        }

        if number_gameball > 0:
            self.current_state = no_quarter_state

    @property
    def can_dispense(self):
        return self.count > 0

    def set_state(self, state):
        self.current_state = self.state_map[state]

    def release_ball(self):
        # System.out.println("ガムボールがスロットから転がり出てきてます");
        if self.count:
            self.count = self.count - 1

    def insert_quarter(self):
        return self.current_state.insert_quarter()

    def eject_quarter(self):
        return self.current_state.eject_quarter()

    def turn_crank(self, force_winner=None):
        return self.current_state.turn_crank(force_winner)

    def dispense(self):
        return self.current_state.dispense()
