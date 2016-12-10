import hashlib


class DoorPasswordCracker:
    def hack(self, door_id: str) -> str:
        index = 0

        result = ''
        md5_hasher = hashlib.md5
        while len(result) < 8:
            md5 = md5_hasher((door_id + str(index)).encode('utf-8')).hexdigest()
            if md5[:5] == '00000':
                result += md5[5]
            index += 1

        return result

    def hack_part_two(self, door_id: str):
        index = 0
        chars_found = 0

        result = list('________')
        md5_hasher = hashlib.md5
        while chars_found < 8:
            md5 = md5_hasher((door_id + str(index)).encode('utf-8')).hexdigest()
            if md5[:5] == '00000':
                if str.isdigit(md5[5]):
                    pos = int(md5[5])
                else:
                    pos = 100
                if pos < 8 and result[pos] == '_':
                    result[pos] = md5[6]
                    chars_found += 1
            index += 1

        return ''.join(result)

if __name__ == '__main__':
    password = DoorPasswordCracker().hack('ugkcyxxp')
    print('Password = ' + password)

    password_door_2 = DoorPasswordCracker().hack_part_two('ugkcyxxp')
    print('Password door 2 = ' + password_door_2)
