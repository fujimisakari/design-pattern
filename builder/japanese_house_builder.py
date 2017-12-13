from .builder import Builder
from .building import Building


class JapaneseHouseBuilder(Builder):

    def __init__(self):
        self.building = Building()

    def build_base(self):
        self.building.base = 'Material.CONCRETE'

    def build_frame(self):
        self.building.frame = 'Material.WOOD'

    def build_wall(self):
        self.building.wall = 'Material.CLAY'

    def get_result(self):
        return self.building
