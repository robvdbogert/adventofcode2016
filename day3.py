def translate_data(lines: list):
    result = []

    for i in range(0, len(lines), 3):
        line1 = get_numbers(lines[i])
        line2 = get_numbers(lines[i+1])
        line3 = get_numbers(lines[i+2])
        result.append('{} {} {}'.format(line1[0], line2[0], line3[0]))
        result.append('{} {} {}'.format(line1[1], line2[1], line3[1]))
        result.append('{} {} {}'.format(line1[2], line2[2], line3[2]))

    return result


def get_numbers(line: str):
    return [int(x) for x in line.split(' ') if x]


class TriangleValidator:
    def validate_sides(self, sides: list) -> bool:
        return sides[0] + sides[1] > sides[2]

    def validate(self, data: str):
        sides = [int(x) for x in data.split(' ') if x]
        sides = sorted(sides)

        return self.validate_sides(sides)


if __name__ == '__main__':
    validator = TriangleValidator()
    with open('./input/day3') as f:
        lines = f.readlines()

    validated = [validator.validate(x) for x in lines if x]
    print('Number of valid triangles: ' + str(len([x for x in validated if x])))

    translated = translate_data(lines)
    validated = [validator.validate(x) for x in translated if x]
    print('Number of valid triangles translated: ' + str(len([x for x in validated if x])))
