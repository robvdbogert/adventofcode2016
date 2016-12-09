import re
from collections import Counter


class RoomValidator:
    _shiftmap = None

    def validate(self, room: str):
        room_regex = re.compile(r'^([a-z-]+)(\d+)\[([a-z]{5})\]$')

        match = room_regex.search(room)
        if match:
            groups = match.groups()
            encrypted_name = groups[0]
            sector_id = int(groups[1])
            checksum = groups[2]
            generated_checksum = self.get_checksum(encrypted_name)
            decrypted_name = self.decrypt_name(encrypted_name, sector_id)
            return checksum == generated_checksum, sector_id, decrypted_name

        return False, None

    def get_checksum(self, encrypted_name: str):
        letter_counts = list(Counter(encrypted_name.replace('-', '')).items())
        letter_counts.sort(key=lambda x: x[0])
        letter_counts.sort(key=lambda x: x[1], reverse=True)
        return ''.join(map(lambda x: x[0], letter_counts))[:5]

    def decrypt_name(self, encrypted_name: str, sector_id: int):
        shift = sector_id % 26
        result = ''
        for letter in encrypted_name:
            if letter == '-':
                result += ' '
            else:
                if ord(letter) + shift > ord('z'):
                    result += chr(ord(letter) - (26 - shift))
                else:
                    result += chr(ord(letter) + shift)
        return result.rstrip()


if __name__ == '__main__':
    with open('./input/day4') as f:
        data = f.readlines()

    validator = RoomValidator()
    sum_sector_ids = 0
    for line in data:
        (valid, sector_id, name) = validator.validate(line)
        if valid:
            sum_sector_ids += sector_id
        if 'north' in name and 'pole' in name:
            print("North Pole objects stored in '{}', sector id '{}'".format(
                name, sector_id
            ))

    print('Sum of sector ids = ' + str(sum_sector_ids))