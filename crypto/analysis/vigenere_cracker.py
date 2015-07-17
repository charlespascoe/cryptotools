import crypto.utils as utils
import crypto.analysis

class VigenereCracker:
    def __init__(self, alph):
        self._caesar_cracker = crypto.analysis.CaesarShiftCracker(alph)
        self._alph = alph

    def guess_key(self, ciphertext, key_length):
        ciphertext = self._alph.strip(ciphertext)

        columns = [[] for i in range(key_length)]

        for i, letter in enumerate(ciphertext):
            columns[i % key_length].append(letter)

        best_key = []

        for column in columns:
            best_key.append(self._alph[self._caesar_cracker.guess_key(''.join(column))])

        return ''.join(best_key)
