from crypto.alphabets import Alphabet
import string

class EnglishAlphabet(Alphabet):
    def __init__(self):
        self._alph = string.ascii_uppercase

    def strip(self, text):
        return super().strip(text.upper())
