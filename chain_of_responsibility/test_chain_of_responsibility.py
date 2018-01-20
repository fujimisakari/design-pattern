import unittest

from .handler_a import HandlerA
from .handler_b import HandlerB


class ChainOfResponsibiity(unittest.TestCase):

    def test_handler(self):
        hand1 = HandlerA('A', 1, 10)
        hand2 = HandlerA('B', 11, 20)
        hand3 = HandlerA('C', 21, 30)
        hand11 = HandlerB('D')
        hand1.set_next(hand2).set_next(hand3).set_next(hand11)
        self.assertEqual(hand1.request(30), 'C：私が成敗してくれるわ!')
