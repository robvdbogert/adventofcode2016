import unittest

from day8 import Display


class TestDisplay(unittest.TestCase):
    def test_process_instruction_with_invalid_param(self):
        display = Display(7, 3)
        with self.assertRaises(ValueError):
            display.process_instruction('blah')

    def test_process_instruction(self):
        display = Display(7, 3)

        display.process_instruction('rect 3x2')
        self.assertEqual([
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ], display.pixels)

        display.process_instruction('rotate column x=1 by 1')
        self.assertEqual([
            [1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0]
        ], display.pixels)

        display.process_instruction('rotate row y=0 by 4')
        self.assertEqual([
            [0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0]
        ], display.pixels)

        display.process_instruction('rotate column x=1 by 1')
        self.assertEqual([
            [0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0]
        ], display.pixels)
