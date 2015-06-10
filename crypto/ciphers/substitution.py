import crypto.utils as utils


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


class CaesarShift(SubstitutionCipher):
    def __init__(self, alph, shift):
        key_mapping = self._generate_mapping(alph, shift)

        super().__init__(alph, key_mapping)

        self._shift = shift

    def _generate_mapping(self, alph, shift):
        if not isinstance(shift, int):
            raise TypeError('shift should be an int')

        return {letter: alph[(alph.index(letter) + shift) % len(alph)] for letter in alph}

    def set_key(self, shift):
        super().set_key(self._generate_mapping(self._alph, shift))


class AffineShift(SubstitutionCipher):
    def __init__(self, alph, a, b):
        key_mapping = self._generate_key_mapping(alph, a, b)

        super().__init__(alph, key_mapping)

        self._a = a
        self._b = b

    def _generate_key_mapping(self, alph, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError('a and b should be integers')

        if utils.gcd(a, len(alph)) != 1:
            raise Exception('a and the length of the alphabet must be coprime')

        return {letter: alph[(a * alph.index(letter) + b) % len(alph)] for letter in alph}

    def set_key(self, a, b):
        super().set_key(self._generate_key_mapping(self._alph, a, b))

