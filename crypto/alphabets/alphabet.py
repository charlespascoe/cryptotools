
class Alphabet:
    def __init__(self):
        self._alph = ''

    def __len__(self):
        return len(self._alph)

    def __getitem__(self, index):
        if index < 0 or index >= len(self._alph):
            raise IndexError()
        return self._alph[index]

    def index(self, item):
        return self._alph.index(item)

    def strip(self, text):
        output = ''
        for char in text:
            if char in self._alph:
                output += char
        return output

    def __iter__(self):
        return iter(self._alph)

    def __str__(self):
        return self._alph

    def __contains__(self, item):
        return item in self._alp