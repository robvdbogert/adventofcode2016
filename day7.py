import re


class IPv7Validator:
    def _get_parts(self, ip):
        return re.split('\[|\]', ip)

    def check_supports_tls(self, ip):
        abba_found = False

        parts = self._get_parts(ip)

        is_hypernet_seq = ip[0] == '['
        for part in parts:
            for i in range(0, len(part)-3):
                group1 = part[i:i+2]
                group2 = part[i+2:i+4]

                if group1[0] != group1[1] and group2 == group1[::-1]:
                    if is_hypernet_seq:
                        return False
                    abba_found = True

            is_hypernet_seq = not is_hypernet_seq

        return abba_found

    def check_supports_ssl(self, ip):
        abas_found = []
        babs_found = []

        parts = self._get_parts(ip)

        is_hypernet_seq = ip[0] == '['
        for part in parts:
            for i in range(0, len(part)-2):
                if part[i] == part[i+2] and part[i] != part[i+1]:
                    seq = part[i:i+3]
                    if not is_hypernet_seq:
                        abas_found.append(seq)
                    else:
                        babs_found.append(seq)

            is_hypernet_seq = not is_hypernet_seq

        for aba in abas_found:
            bab = aba[1] + aba[0] + aba[1]
            if bab in babs_found:
                return True

        return False


if __name__ == '__main__':
    with open('./input/day7') as f:
        data = f.read().split()

    validator = IPv7Validator()
    nr_ips_supporting_tls = 0
    nr_ips_supporting_ssl = 0
    for ip in data:
        if validator.check_supports_tls(ip):
            nr_ips_supporting_tls += 1
        if validator.check_supports_ssl(ip):
            nr_ips_supporting_ssl += 1

    print('Number of ip\'s supporting TLS: ' + str(nr_ips_supporting_tls))
    print('Number of ip\'s supporting SSL: ' + str(nr_ips_supporting_ssl))
