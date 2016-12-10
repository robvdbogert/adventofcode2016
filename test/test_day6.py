import unittest

from day6 import MessageRecovery


class TestMessageRecovery(unittest.TestCase):
    def test_recover(self):
        data = [
            'eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar'
        ]

        message = MessageRecovery().get_message(data)
        self.assertEqual('easter', message)
