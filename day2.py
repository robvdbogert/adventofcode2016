class CodeCalculator:
    _keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    def __init__(self, code_data):
        self._code_data = code_data

    def get_code(self, start_button):
        current_x = None
        current_y = None

        for y in range(0, len(self._keypad)):
            for x in range(0, len(self._keypad[0])):
                if self._keypad[y][x] == start_button:
                    current_x = x
                    current_y = y
                    break
            if current_x is not None:
                break

        code = ''
        for line in self._code_data:
            for instruction in line:
                next_x = current_x
                next_y = current_y
                if instruction == 'U':
                    next_y = current_y - 1
                elif instruction == 'D':
                    next_y = current_y + 1
                elif instruction == 'L':
                    next_x = current_x - 1
                elif instruction == 'R':
                    next_x = current_x + 1

                if 0 <= next_y < len(self._keypad) and 0 <= next_x < len(self._keypad[0]):
                    if self._keypad[next_y][next_x] is not None:
                        current_x = next_x
                        current_y = next_y

            button_to_press = self._keypad[current_y][current_x]
            code += str(button_to_press)

        return code

    def set_keypad(self, keypad):
        self._keypad = keypad

if __name__ == '__main__':
    with open('./input/day2') as f:
        data = f.readlines()

    calc = CodeCalculator(data)
    code = calc.get_code(5)
    print('code = {}'.format(code))

    calc = CodeCalculator(data)
    calc.set_keypad([
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ])
    code = calc.get_code(5)
    print('code = {}'.format(code))
