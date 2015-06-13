import crypto.utils as utils
import crypto.alphabets
import crypto.ciphers


class CaesarShiftCracker:
    def __init__(self, alph):
        if not isinstance(alph, crypto.alphabets.AlphabetWithProbabilities):
            raise TypeError('alph must be an AlphabetWithProbabilities')

        self._alph = alph

    def guess_key(self, ciphertext):
        ciphertext = self._alph.strip(ciphertext)

        probs = utils.compute_probabilities(ciphertext, self._alph)

        best_weight = 1000000
        best_shift = 0

        for shift in range(len(self._alph)):
            w = self.calculate_weight(probs, self._alph.probs, shift)

            if w < best_weight:
                best_weight = w
                best_shift = shift

        return best_shift

    def calculate_weight(self, probs, expected_probs, shift):
        weight = 0

        for i in range(len(self._alph)):
            weight += abs(expected_probs[i] - probs[(i + shift) % len(self._alph)])

        return weight
