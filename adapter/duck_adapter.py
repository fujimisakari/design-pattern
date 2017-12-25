from .turkey import Turkey


class DuckAdapter(Turkey):

    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        return self.duck.quack()

    def fly(self):
        return self.duck.fly()
