import unittest

from day4 import RoomValidator


class TestRoomValidator(unittest.TestCase):
    def test_validate(self):
        validator = RoomValidator()

        (valid, sector_id, name) = validator.validate('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertTrue(valid)

        (valid, sector_id, name) = validator.validate('bbbbb-aaa-z-y-x-123[baxyz]')
        self.assertTrue(valid)

        (valid, sector_id, name) = validator.validate('a-b-c-d-e-f-g-h-987[abcde]')
        self.assertTrue(valid)

        (valid, sector_id, name) = validator.validate('not-a-real-room-404[oarel]')
        self.assertTrue(valid)

        (valid, sector_id, name) = validator.validate('totally-real-room-200[decoy]')
        self.assertFalse(valid)

        (valid, sector_id, name) = validator.validate('qzmt-zixmtkozy-ivhz-343[blaat]')
        self.assertEqual('very encrypted name', name)