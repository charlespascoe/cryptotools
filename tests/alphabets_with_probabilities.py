from crypto.alphabets import Alphabet

class AlphabetWithProbabilities(Alphabet):
    def __init__(self):
        super().__init__()
        self.probs = None

    def init_probs(self):
        raise NotImplemented()

    def prob(self, char):
        if probs is None:
            self.init_probs()

        if not char in self:
            return 0

        return self.probs[self.index(char)]



