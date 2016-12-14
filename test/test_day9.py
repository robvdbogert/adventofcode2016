import unittest

from day9 import Decompressor


class TestDecompressor(unittest.TestCase):
    def test_decompress(self):
        decompressor = Decompressor()

        self.assertEqual('ADVENT', decompressor.decompress('ADVENT'))
        self.assertEqual('ABBBBBC', decompressor.decompress('A(1X5)BC'))
        self.assertEqual('XYZXYZXYZ', decompressor.decompress('(3X3)XYZ'))
        self.assertEqual('ABCBCDEFEFG', decompressor.decompress('A(2X2)BCD(2X2)EFG'))
        self.assertEqual('(1X3)A', decompressor.decompress('(6X1)(1X3)A'))
        self.assertEqual('X(3X3)ABC(3X3)ABCY', decompressor.decompress('X(8X2)(3X3)ABCY'))
        self.assertEqual('(3x1)(1x1)(3x1)(1x1)AAP', decompressor.decompress('(10x2)(3x1)(1x1)AAP'))

    def test_get_decompressed_length(self):
        decompressor = Decompressor()

        self.assertEqual(20, decompressor.get_decompressed_length('X(8x2)(3x3)ABCY'))
        self.assertEqual(9, decompressor.get_decompressed_length('(3X3)XYZ'))
        self.assertEqual(241920, decompressor.get_decompressed_length('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
        self.assertEqual(445, decompressor.get_decompressed_length(
            '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))