import crypto.utils as utils
import crypto.alphabets
import crypto.ciphers


class AffineShiftCracker:
    def __init__(self, alph):
        self._caesar_cracker = crypto.analysis.CaesarShiftCracker(alph)
        self._alph = alph

    def guess_key(self, ciphertext):
        best_a = 1
        best_b = 0
        best_weight = 1000000

        afs = crypto.ciphers.AffineShiftCipher(self._alph, 1, 0)

        for a in utils.compute_coprimes(len(self._alph)):
            afs.set_key(a, 0)

            shift_text = afs.decrypt(ciphertext)

            # x = (b * a_inv) mod len(alphabet)
            x, weight = self._caesar_cracker.guess_key(shift_text, True)

            if weight < best_weight:
                best_a = a
                best_b = (x * a) % len(self._alph)
                best_weight = weight

        return (best_a, best_b)
