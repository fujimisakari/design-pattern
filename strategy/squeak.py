from .interface import QuackBehaviorInterface


class Squeak(QuackBehaviorInterface):

    def quack(self):
        return 'キューキュー'
