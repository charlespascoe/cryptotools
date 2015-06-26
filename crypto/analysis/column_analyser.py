import crypto.utils as utils


class ColumnAnalyser:
    def __init__(self, alph):
        self._alph = alph

    def analyse(self, text, upper_limit):
        vals = [self._alph.index(letter) for letter in self._alph.strip(text)]

        iocs = [0] * (upper_limit + 1)

        for num_cols in range(1, upper_limit + 1):
            cols = [[0 for i in range(len(self._alph))] for j in range(num_cols)]

            pos = 0

            for x in vals:
                cols[pos][x] += 1
                pos = (pos + 1) % len(cols)

            mean_ioc = 0

            for freqs in cols:
                mean_ioc += utils.index_of_coincidence(freqs)

            mean_ioc /= len(cols)

            iocs[num_cols] = mean_ioc

        return iocs
