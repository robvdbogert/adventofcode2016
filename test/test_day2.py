import unittest

from day2 import CodeCalculator


class TestCodeCalculator(unittest.TestCase):
    def test_get_code(self):
        code_data = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]

        calc = CodeCalculator(code_data)
        self.assertEqual('1985', calc.get_code(5))

    def test_get_code_custom_keypad(self):
        code_data = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]

        calc = CodeCalculator(code_data)
        calc.set_keypad([
            [None, None, 1, None, None],
            [None, 2, 3, 4, None],
            [5, 6, 7, 8, 9],
            [None, 'A', 'B', 'C', None],
            [None, None, 'D', None, None]
        ])

        code = calc.get_code(5)
        self.assertEqual('5DB3', code)
