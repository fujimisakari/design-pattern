import unittest

from .director import Director
from .japanese_house_builder import JapaneseHouseBuilder
from .kamakura_builder import KamakuraBuilder


class BuilderTest(unittest.TestCase):

    def test_japanese_house_builder(self):
        director = Director(JapaneseHouseBuilder())
        japanese_house = director.construct()

        self.assertEqual(japanese_house.base, 'Material.CONCRETE')
        self.assertEqual(japanese_house.frame, 'Material.WOOD')
        self.assertEqual(japanese_house.wall, 'Material.CLAY')

    def test_kamakura_builder(self):
        director = Director(KamakuraBuilder())
        kamakura = director.construct()

        self.assertEqual(kamakura.base, 'Material.SNOW')
        self.assertEqual(kamakura.frame, 'Material.SNOW')
        self.assertEqual(kamakura.wall, 'Material.SNOW')
