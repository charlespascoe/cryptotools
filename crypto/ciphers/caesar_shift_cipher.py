from crypto.ciphers import SubstitutionCipher

class CaesarShiftCipher(SubstitutionCipher):
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