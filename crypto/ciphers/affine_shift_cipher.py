from crypto.ciphers import SubstitutionCipher
import crypto.utils as utils

class AffineShiftCipher(SubstitutionCipher):
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
