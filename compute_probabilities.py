import crypto.alphabets
import crypto.utils as utils
import sys
import json


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You need to provide an alphabet name and a destination file')
        sys.exit(0)

    alph_name = sys.argv[1]
    file_name = sys.argv[2]

    if not alph_name in dir(crypto.alphabets):
        print('Invalid alphabet name:', alph_name)
        sys.exit(0)

    alph = getattr(crypto.alphabets, alph_name)()

    text = sys.stdin.read()

    probs = utils.compute_probabilities(text, alph)

    data = {
        'probs': probs,
        'digram-probs': None,
        'trigram-probs': None
    }

    with open(file_name, 'w') as f:
        f.write(json.dumps(data))
