from .quack import Quack


class Duck():

    def __init__(self):
        self.quack_behavior = Quack()

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_quack(self):
        return self.quack_behavior.quack()
