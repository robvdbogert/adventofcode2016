import re


class Display:
    _rect_regex = re.compile('^rect ([\d]+)x([\d]+)$')
    _rotate_row_regex = re.compile('^rotate row y=([\d]+) by ([\d]+)')
    _rotate_col_regex = re.compile('^rotate column x=([\d]+) by ([\d]+)')

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0 for x in range(0, width)] for y in range(0, height)]

    def process_instruction(self, instruction):
        rect_instruction = self._rect_regex.search(instruction)
        if rect_instruction:
            self.rect(rect_instruction)
            return

        rotate_row_instruction = self._rotate_row_regex.search(instruction)
        if rotate_row_instruction:
            self.rotate_row(rotate_row_instruction)
            return

        rotate_column_instruction = self._rotate_col_regex.search(instruction)
        if rotate_column_instruction:
            self.rotate_column(rotate_column_instruction)
            return

        raise ValueError("Unknown instruction '{}'".format(instruction))

    def rect(self, rect_instruction):
        rw = int(rect_instruction.group(1))
        rh = int(rect_instruction.group(2))
        for y in range(0, rh):
            for x in range(0, rw):
                self.pixels[y][x] = 1

    def rotate_column(self, rotate_column_instruction):
        # Shift pixels down (and bottom -> top if they fall off)
        col = int(rotate_column_instruction.group(1))
        amount = int(rotate_column_instruction.group(2))

        # Get all pixels in the column
        v_line = []
        for y in range(0, self.height):
            v_line.append(self.pixels[y][col])

        for y in range(0, self.height):
            self.pixels[y][col] = v_line[y - amount]

    def rotate_row(self, rotate_row_instruction):
        # Shift pixels right (and right -> left if they fall off)
        row = int(rotate_row_instruction.group(1))
        amount = int(rotate_row_instruction.group(2))

        h_line = self.pixels[row][:]

        for x in range(0, self.width):
            self.pixels[row][x] = h_line[x - amount]

    def show(self):
        for line in self.pixels:
            text = ''.join(['#' if x else ' ' for x in line])
            print(text)
        print('\n')


if __name__ == '__main__':
    with open('./input/day8') as f:
        data = f.readlines()

    display = Display(50, 6)
    for instruction in data:
        display.process_instruction(instruction)

    count = 0
    for line in display.pixels:
        for pixel in line:
            if pixel:
                count += 1

    display.show()

    print('Number of lit pixels = ' + str(count))
