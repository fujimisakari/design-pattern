import unittest

from .duck_adapter import DuckAdapter
from .mallard_duck_adaptee import MallardDuckAdaptee


class AdapterTest(unittest.TestCase):

    def setUp(self):
        duck = MallardDuckAdaptee()
        self.duck_adapter = DuckAdapter(duck)

    def test_adapter_gobble(self):
        self.assertEqual('Quack', self.duck_adapter.gobble())

    def test_adapter_fly(self):
        self.assertEqual('Im flying', self.duck_adapter.fly())
