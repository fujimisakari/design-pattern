import unittest

from .condiment.milk import Milk
from .condiment.whip import Whip
from .dark_roast import DarkRoast


class DecoratorTest(unittest.TestCase):

    def setUp(self):
        self.darkRoast = DarkRoast()

    def test_decorator_coffee_name(self):
        self.assertEqual('ダークロースト', self.darkRoast.get_description())

    def test_decorator_coffee_cost(self):
        self.assertEqual(340, self.darkRoast.cost())

    def test_decorator_coffee_name_with_milk(self):
        darkRoast = Milk(self.darkRoast)
        self.assertEqual('ダークロースト、ミルク入り', darkRoast.get_description())

    def test_decorator_coffee_cost_with_milk(self):
        darkRoast = Milk(self.darkRoast)
        self.assertEqual(370, darkRoast.cost())

    def test_decorator_coffee_name_with_milk_and_whip(self):
        darkRoast = Milk(self.darkRoast)
        darkRoast = Whip(darkRoast)
        self.assertEqual('ダークロースト、ミルク入り、ホイップ入り', darkRoast.get_description())

    def test_decorator_coffee_cost_with_milk_and_whip(self):
        darkRoast = Milk(self.darkRoast)
        darkRoast = Whip(darkRoast)
        self.assertEqual(400, darkRoast.cost())
