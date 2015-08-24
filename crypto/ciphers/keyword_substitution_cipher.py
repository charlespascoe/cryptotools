from crypto.ciphers import SubstitutionCipher


class KeywordSubstitutionCipher(SubstitutionCipher):
    def __init__(self, alph, keyword):
        key_mapping = self._generate_key_mapping(alph, keyword)

        super().__init__(alph, key_mapping)

        self._keyword = keyword

    def _generate_key_mapping(self, alph, keyword):
        key = {}

        a = iter(alph)

        for letter in alph.strip(keyword) + str(alph):
            if letter not in key.values():
                key[next(a)] = letter

        return key
