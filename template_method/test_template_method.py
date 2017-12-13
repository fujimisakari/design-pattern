import unittest

from .coffee import Coffee
from .tea import Tea


class TemplateMethodTest(unittest.TestCase):

    def test_coffee_brew(self):
        coffee = Coffee()
        self.assertEqual(coffee.brew(), 'Dripping Coffee through filter')

    def test_coffee_add_condiments(self):
        coffee = Coffee()
        self.assertEqual(coffee.add_condiments(), 'Adding Sugar and Milk')

    def test_coffee_boil_water(self):
        coffee = Coffee()
        self.assertEqual(coffee.boil_water(), 'Boiling water')

    def test_coffee_pour_in_cup(self):
        coffee = Coffee()
        self.assertEqual(coffee.pour_in_cup(), 'Pouring into cup')

    def test_tea_brew(self):
        tea = Tea()
        self.assertEqual(tea.brew(), 'Steeping the tea')

    def test_tea_add_condiments(self):
        tea = Tea()
        self.assertEqual(tea.add_condiments(), 'Adding Lemon')

    def test_tea_boil_water(self):
        tea = Tea()
        self.assertEqual(tea.boil_water(), 'Boiling water')

    def test_tea_pour_in_cup(self):
        tea = Tea()
        self.assertEqual(tea.pour_in_cup(), 'Pouring into cup')
