class MessageRecovery:
    def get_message(self, data, use_most_common_letter=True):
        letter_counts = [{} for x in range(0, len(data[0]))]

        for line in data:
            for index, char in enumerate(line):
                if char not in letter_counts[index]:
                    letter_counts[index][char] = 0
                letter_counts[index][char] += 1

        result = ''.join([sorted(x, key=lambda k: x[k], reverse=use_most_common_letter)[0] for x in letter_counts])
        return result


if __name__ == '__main__':
    with open('./input/day6') as f:
        data = f.read().split()

    recovery = MessageRecovery()
    message = recovery.get_message(data)
    print('Message using most common letter in each column: ' + message)

    message = recovery.get_message(data, False)
    print('Message using least common letter in each column: ' + message)