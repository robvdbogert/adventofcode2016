import unittest

from day6 import MessageRecovery


class TestMessageRecovery(unittest.TestCase):
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

    def test_recover_using_most_common_letter(self):
        message = MessageRecovery().get_message(self.data)
        self.assertEqual('easter', message)

    def test_recover_using_least_common_letter(self):
        message = MessageRecovery().get_message(self.data, False)
        self.assertEqual('advent', message)
