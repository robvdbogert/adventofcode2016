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


if __name__ == '__main__':
    password = DoorPasswordCracker().hack('ugkcyxxp')
    print('Password = ' + password)
