from crypto.alphabets import AlphabetWithProbabilities
import string


class EnglishAlphabet(AlphabetWithProbabilities):
    def __init__(self):
        super().__init__()
        self._alph = string.ascii_uppercase

    def strip(self, text):
        return super().strip(text.upper())
