import enum


class GumballMachineStat(enum.IntEnum):
    HAS_QUARTER = 1
    SOLD = 2
    SOLD_OUT = 3
    NO_QUARTER = 4
    WINNER = 5
