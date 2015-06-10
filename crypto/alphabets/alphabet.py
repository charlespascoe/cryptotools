

class Alphabet:
    def __init__(self):
        self._alph = ''

    def __len__(self):
        return len(self._alph)

    def __getitem__(self, index):
        return self._alph[index]

    def index(self, item):
        return self._alph.index(item)

    def strip(self, text):
        return ''.join([letter for letter in text if letter in self])

    def __iter__(self):
        return iter(self._alph)

    def __str__(self):
        return self._alph

    def __contains__(self, item):
        return item in self._alph
