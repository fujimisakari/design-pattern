from .builder import Builder
from .building import Building


class KamakuraBuilder(Builder):

    def __init__(self):
        self.building = Building()

    def build_base(self):
        self.building.base = 'Material.SNOW'

    def build_frame(self):
        self.building.frame = 'Material.SNOW'

    def build_wall(self):
        self.building.wall = 'Material.SNOW'

    def get_result(self):
        return self.building
