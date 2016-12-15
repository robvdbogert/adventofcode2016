import re


class BotBalancer:
    _RECEIVES_REGEX = re.compile('^value (\d+) goes to bot (\d+)$')
    _PASS_REGEX = re.compile('^bot (\d+) gives low to (bot|output) (\d+) and high to (output|bot) (\d+)$')

    def __init__(self, instructions: list):
        self.bot_logic = {}
        self.log = []
        self.outputs = {}

        for instruction in instructions:
            match = self._RECEIVES_REGEX.match(instruction)
            if match:
                value = int(match.group(1))
                bot = int(match.group(2))

                self.add_bot_if_missing(bot)

                self.bot_logic[bot]['input'].append(value)
                continue

            match = self._PASS_REGEX.match(instruction)
            if match:
                bot = int(match.group(1))
                low_type = match.group(2)
                low_nr = int(match.group(3))
                high_type = match.group(4)
                high_nr = int(match.group(5))

                self.add_bot_if_missing(bot)

                self.bot_logic[bot]['low_' + low_type] = low_nr
                self.bot_logic[bot]['high_' + high_type] = high_nr
                continue

            raise ValueError("Invalid instruction '{}'".format(instruction))

    def start(self):
        # Check what bot has two value chips
        (bot, bot_nr) = next((self.bot_logic[x], x) for x in self.bot_logic if len(self.bot_logic[x]['input']) > 1)
        while bot:
            self.log.append('bot {} compares values {}'.format(bot_nr, sorted(bot['input'])))
            (low, high) = sorted(bot['input'])
            if bot['low_bot'] is not None:
                self.bot_logic[bot['low_bot']]['input'].append(low)
            elif bot['low_output'] is not None:
                self.outputs[bot['low_output']] = low
            bot['input'].remove(low)
            if bot['high_bot'] is not None:
                self.bot_logic[bot['high_bot']]['input'].append(high)
            elif bot['high_output'] is not None:
                self.outputs[bot['high_output']] = high
            bot['input'].remove(high)

            try:
                (bot, bot_nr) = next(
                    (self.bot_logic[x], x) for x in self.bot_logic if len(self.bot_logic[x]['input']) > 1)
            except:
                bot = None

    def add_bot_if_missing(self, bot_nr):
        if bot_nr not in self.bot_logic:
            self.bot_logic[bot_nr] = {
                'input': [],
                'low_bot': None,
                'low_output': None,
                'high_bot': None,
                'high_output': None
            }


if __name__ == '__main__':
    with open('./input/day10') as f:
        data = f.readlines()

    balancer = BotBalancer(data)
    balancer.start()

    line = next(s for s in balancer.log if 'compares values [17, 61]' in s)
    print(line)

    print('Multiplied values of outputs 0, 1, 2 = {} x {} x {} = {}'.format(
        balancer.outputs[0], balancer.outputs[1], balancer.outputs[2],
        balancer.outputs[0] * balancer.outputs[1] * balancer.outputs[2]
    ))
