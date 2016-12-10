import unittest

from day5 import DoorPasswordCracker


class TestDoorPasswordCracker(unittest.TestCase):
    def test_hack(self):
        cracker = DoorPasswordCracker()
        password = cracker.hack('abc')
        self.assertEqual('18f47a30', password)

    def test_hack_part_two(self):
        cracker = DoorPasswordCracker()
        password = cracker.hack_part_two('abc')
        self.assertEqual('05ace8e3', password)