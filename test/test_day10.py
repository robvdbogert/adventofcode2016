import unittest

from day10 import BotBalancer


class TestBotBalancer(unittest.TestCase):
    instructions = [
        'value 5 goes to bot 2',
        'bot 2 gives low to bot 1 and high to bot 0',
        'value 3 goes to bot 1',
        'bot 1 gives low to output 1 and high to bot 0',
        'bot 0 gives low to output 2 and high to output 0',
        'value 2 goes to bot 2'
    ]

    def test_init(self):
        balancer = BotBalancer(self.instructions)
        self.assertIn(2, balancer.bot_logic)
        self.assertIn(1, balancer.bot_logic)

        self.assertEqual([5, 2], balancer.bot_logic[2]['input'])
        self.assertEqual([3], balancer.bot_logic[1]['input'])

        self.assertEqual(1, balancer.bot_logic[2]['low_bot'])
        self.assertEqual(0, balancer.bot_logic[2]['high_bot'])

        self.assertEqual(1, balancer.bot_logic[1]['low_output'])
        self.assertEqual(0, balancer.bot_logic[1]['high_bot'])

    def test_start(self):
        balancer = BotBalancer(self.instructions)
        balancer.start()
