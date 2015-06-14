from crypto.alphabets import Alphabet


class AlphabetWithProbabilities(Alphabet):
    def __init__(self):
        super().__init__()
        self.probs = None

    def init_probs(self, prob_loader):
        data = prob_loader.load(self.__class__.__name__)

        if data is None:
            return False

        self.probs = data['probs']

        return True

    def prob(self, letter):
        if self.probs is None:
            raise Exception('Probabilities have not be initialised')

        if not letter in self:
            return 0

        return self.probs[self.index(letter)]
