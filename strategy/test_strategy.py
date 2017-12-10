import unittest

from .duck import Duck
from .squeak import Squeak


class StrategyDockTest(unittest.TestCase):

    def setUp(self):
        self.duck = Duck()

    def test_strategy_dock_quack(self):
        self.assertEqual('ガーガー', self.duck.perform_quack())

    def test_strategy_duck_squeak(self):
        self.duck.set_quack_behavior(Squeak())
        self.assertEqual('キューキュー', self.duck.perform_quack())
