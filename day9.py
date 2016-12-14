import re

marker_regex = re.compile(r'\(([\d]+)[X|x]([\d]+)\)')


class Decompressor:
    def decompress(self, data):
        matches = marker_regex.finditer(data)
        result = ''
        last_pos = 0
        for match in matches:
            if match.span()[0] < last_pos:
                # Skip markers inside markers
                continue
            # First store the data from the end of the last match to the start of the next
            result += data[last_pos:match.span()[0]]

            nr_chars = int(match.group(1))
            nr_repetitions = int(match.group(2))

            group_to_repeat = data[match.span()[1]:match.span()[1] + nr_chars]
            for i in range(0, nr_repetitions):
                result += group_to_repeat

            last_pos = match.span()[1]+nr_chars

        result += data[last_pos:]
        return result

    def get_decompressed_length(self, data):
        length = 0
        matches = marker_regex.finditer(data)
        end = 0
        for match in matches:
            if match.span()[0] < end:
                continue

            # Add the characters from the end of the last match to the start of this one
            length += match.span()[0] - end

            start = match.span()[1]
            end = start + int(match.group(1))
            match_content = data[start:end]
            nr_repetitions = int(match.group(2))

            if marker_regex.match(match_content):
                length += nr_repetitions * self.get_decompressed_length(match_content)
            else:
                length += nr_repetitions * len(match_content)

        # Add the characters from the end of the last match to the end of the data
        length += len(data) - end

        return length


if __name__ == '__main__':
    with open('./input/day9') as f:
        data = f.read().strip()

    # Part 1
    decompressor = Decompressor()
    decompressed = decompressor.decompress(data)
    print('Decompressed size: {}'.format(len(decompressed)))

    # Part 2
    length = decompressor.get_decompressed_length(data)
    print('Length of completely decompressed data: {}'.format(length))