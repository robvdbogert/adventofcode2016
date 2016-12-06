import time
from collections import OrderedDict


class DistanceCalculator:

    _headings = {
        'N': {
            'R': 'E',
            'L': 'W'
        },
        'E': {
            'R': 'S',
            'L': 'N'
        },
        'S': {
            'R': 'W',
            'L': 'E'
        },
        'W': {
            'R': 'N',
            'L': 'S'
        }
    }

    def __init__(self, data):
        self._data = data
        self._elements = [(x[0], int(x[1:])) for x in data.split(', ')]

    def calculate_visit_count(self):
        history = OrderedDict()

        north = 0
        east = 0
        current_heading = 'N'

        for e in self._elements:
            (direction, steps) = e
            next_heading = self._headings[current_heading][direction]
            for i in range(0, steps):
                if next_heading == 'N':
                    north += 1
                elif next_heading == 'S':
                    north -= 1
                elif next_heading == 'E':
                    east += 1
                elif next_heading == 'W':
                    east -= 1

                location = north, east
                if location not in history:
                    history[location] = 0
                history[location] += 1

                current_heading = next_heading

        return history

    def calculate_distance(self):
        total_north = 0
        total_east = 0
        current_heading = 'N'

        for e in self._elements:
            direction, steps = e

            next_heading = self._headings[current_heading][direction]
            if next_heading == 'N':
                total_north += steps
            elif next_heading == 'S':
                total_north -= steps
            elif next_heading == 'E':
                total_east += steps
            elif next_heading == 'W':
                total_east -= steps

            current_heading = next_heading

        return total_north, total_east


if __name__ == '__main__':
    with open('./input/day1') as f:
        data = f.readline()

    calculator = DistanceCalculator(data)
    (north, east) = calculator.calculate_distance()
    print('total blocks: {}'.format(abs(north) + abs(east)))

    history = calculator.calculate_visit_count()
    print(history)

    for loc in history:
        if history[loc] > 1:
            print('{} visited {} times, {} blocks away'.format(loc, history[loc], loc[0] + loc[1]))
            break
