import unittest

from day4 import RoomValidator


class TestRoomValidator(unittest.TestCase):
    def test_validate(self):
        validator = RoomValidator()

        (valid, sector_id) = validator.validate('aaaaa-bbb-z-y-x-123[abxyz]')
        self.assertTrue(valid)

        (valid, sector_id) = validator.validate('bbbbb-aaa-z-y-x-123[baxyz]')
        self.assertTrue(valid)

        (valid, sector_id) = validator.validate('a-b-c-d-e-f-g-h-987[abcde]')
        self.assertTrue(valid)

        (valid, sector_id) = validator.validate('not-a-real-room-404[oarel]')
        self.assertTrue(valid)

        (valid, sector_id) = validator.validate('totally-real-room-200[decoy]')
        self.assertFalse(valid)
