import unittest

from day5 import DoorPasswordCracker


class TestDoorPasswordCracker(unittest.TestCase):
    def test_crack(self):
        cracker = DoorPasswordCracker()
        password = cracker.hack('abc')
        self.assertEqual('18f47a30', password)