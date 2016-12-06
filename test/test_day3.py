import unittest

from day3 import TriangleValidator, translate_data


class TestTriangleValidator(unittest.TestCase):
    def test_validate_triangle(self):
        validator = TriangleValidator()

        valid = validator.validate('5 10 25')
        self.assertFalse(valid)

        valid = validator.validate('3 4 5')
        self.assertTrue(valid)

        valid = validator.validate('25 10 5')
        self.assertFalse(valid)

    def test_translate_data(self):
        data = [
            '10 20 30',
            '5 8 6',
            '7 9 10'
        ]

        translated_data = translate_data(data)
        self.assertEqual([
            '10 5 7',
            '20 8 9',
            '30 6 10'
        ], translated_data)