import crypto.utils as utils


class AffineShift:
    def __init__(self, alph):
        self.alph = alph

    def encrypt(self, a, b, text):
        if not utils.is_coprime(a, len(self.alph)):
            raise Exception('\'a\' and the length of the alphabet must be coprime')

        output = []

        for char in self.alph.strip(text):
            output.append(self.alph[(a * self.alph.index(char) + b) % len(self.alph)])

        return ''.join(output)

    def decrypt(self, a, b, text):
        inv_a = utils.compute_inverse(a, len(self.alph))
        inv_b = -inv_a * b

        return self.encrypt(inv_a, inv_b, text)
