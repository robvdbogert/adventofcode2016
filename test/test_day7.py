import unittest

from day7 import IPv7Validator


class TestIPv7Validator(unittest.TestCase):
    def test_check_supports_tls(self):
        validator = IPv7Validator()
        self.assertTrue(validator.check_supports_tls('abba[mnop]qrst'))
        self.assertFalse(validator.check_supports_tls('abcd[bddb]xyyx'))
        self.assertFalse(validator.check_supports_tls('aaaa[qwer]tyui'))
        self.assertTrue(validator.check_supports_tls('ioxxoj[asdfgh]zxcvbn'))

    def test_check_supports_ssl(self):
        validator = IPv7Validator()
        self.assertTrue(validator.check_supports_ssl('aba[bab]xyz'))
        self.assertFalse(validator.check_supports_ssl('xyx[xyx]xyx'))
        self.assertTrue(validator.check_supports_ssl('aaa[kek]eke'))
        self.assertTrue(validator.check_supports_ssl('zazbz[bzb]cdb'))
