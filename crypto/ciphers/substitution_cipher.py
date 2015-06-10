
class SubstitutionCipher:
    def __init__(self, alph, key_mapping):
        if not isinstance(key_mapping, dict):
            raise TypeError('key_mapping must be a dict')

        self._alph = alph

        self._set_key_mapping(key_mapping)

    def _set_key_mapping(self, key_mapping):
        if not SubstitutionCipher.is_valid_key(self._alph, key_mapping):
            raise Exception('key_mapping must be bijective and its range and domain must be the provided alphabet')

        self._key_mapping = key_mapping

    def set_key(self, key_mapping):
        self._set_key_mapping(key_mapping)

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

    @classmethod
    def invert_mapping(self, mapping):
        return {value: key for key, value in mapping.items()}

    def encrypt(self, text):
        return ''.join([self._key_mapping[letter] for letter in text if letter in self._key_mapping])

    def decrypt(self, text):
        decryption_mapping = SubstitutionCipher.invert_mapping(self._key_mapping)
        return ''.join([decryption_mapping[letter] for letter in text if letter in decryption_mapping])
