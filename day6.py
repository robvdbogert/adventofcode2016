class MessageRecovery:
    def get_message(self, data):
        letter_counts = [{} for x in range(0, len(data[0]))]

        for line in data:
            for index, char in enumerate(line):
                if char not in letter_counts[index]:
                    letter_counts[index][char] = 0
                letter_counts[index][char] += 1

        result = ''.join([sorted(x, key=lambda k: x[k], reverse=True)[0] for x in letter_counts])
        return result


if __name__ == '__main__':
    with open('./input/day6') as f:
        data = f.read().split()

    message = MessageRecovery().get_message(data)
    print('Message: ' + message)