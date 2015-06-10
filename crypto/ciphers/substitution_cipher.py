
class SubstitutionCipher:
    def __init__(self, alph, key_mapping):
        if not isinstance(key_mapping, dict):
            raise TypeError('key_mapping must be a dict')

        self._alph = alph

        self.set_key(key_mapping)

    def set_key(self, key_mapping):
        if not SubstitutionCipher.is_valid_key(self._alph, key_mapping):
            raise Exception('key_mapping must be bijective and its range and domain must be the provided alphabet')

        self._key = key_mapping

    @classmethod
    def is_valid_key(cls, alph, mapping):
        domain = [letter for letter in alph]

        for letter in alph:
            if letter not in mapping:
                return False

            output = mapping[letter]

            if output not in domain:
                return False

            domain.remove(output)

        return len(domain) == 0

    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass
