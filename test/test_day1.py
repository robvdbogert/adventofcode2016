import unittest

from day1 import DistanceCalculator

test_data = {
    'R2, L3': 5,
    'R2, R2, R2': 2,
    'R5, L5, R5, R3': 12
}


class TestDistanceCalculator(unittest.TestCase):
    def test_calculate_distance(self):
        for data in test_data:
            (north, east) = DistanceCalculator(data).calculate_distance()
            self.assertEqual(test_data[data], abs(north) + abs(east))

    def test_calculate_visit_count(self):
        data = 'R8, R4, R4, R8'
        history = DistanceCalculator(data).calculate_visit_count()
        for loc in history:
            if history[loc] > 1:
                self.assertEqual((0, 4), loc)
                break
