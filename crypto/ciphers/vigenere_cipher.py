
class VigenereCipher:
    def __init__(self, alph, keyword):
        self._alph = alph
        self.set_key(keyword)

    def set_key(self, keyword):
        keyword = self._alph.strip(keyword)

        if len(keyword) == 0:
            raise Exception('No valid keyword provided')

        self._keyword = keyword

    def encrypt(self, text):
        text = self._alph.strip(text)
        output = []

        k = [self._alph.index(letter) for letter in self._keyword]

        for i, letter in enumerate(text):
            output.append(self._alph[(self._alph.index(letter) + k[i % len(k)]) % len(self._alph)])

        return ''.join(output)

    def decrypt(self, text):
        text = self._alph.strip(text)
        output = []

        k = [self._alph.index(letter) for letter in self._keyword]

        for i, letter in enumerate(text):
            output.append(self._alph[(self._alph.index(letter) - k[i % len(k)]) % len(self._alph)])

        return ''.join(output)