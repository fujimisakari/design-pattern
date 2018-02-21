import unittest

from .client import Client
from .prototype import ConcretePrototype


class PrototypeTest(unittest.TestCase):

    def test_prototype(self):
        cp1 = ConcretePrototype(1)
        cp2 = ConcretePrototype(2)
        cp3 = ConcretePrototype(3)
        client = Client()
        client.regist('cp1', cp1)
        client.regist('cp2', cp2)
        client.regist('cp3', cp3)
        self.assertEqual(client.create('cp1').get_type_id(), 1)
        self.assertEqual(client.create('cp2').get_type_id(), 2)
        self.assertEqual(client.create('cp3').get_type_id(), 3)
