
class Director():

    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_base()
        self.builder.build_frame()
        self.builder.build_wall()
        return self.builder.get_result()
