import crypto.alphabets
import crypto.analysis
import crypto.ciphers

def create_parsers(parser):
    analysis_parser = parser.add_parser('analysis', help='Analysis things')

    subparsers = analysis_parser.add_subparsers(help=   'Analysis tools')

    caesar_shift_cracker_parser = subparsers.add_parser('caesar-shift-cracker', help='Cracks caesar shift')
    caesar_shift_cracker_parser.set_defaults(func=crack_caesar)

def crack_caesar(args, src, log, dst):
    pl = crypto.alphabets.ProbabilityLoader('crypto/alphabets/data')

    alph = crypto.alphabets.EnglishAlphabet()

    if not alph.init_probs(pl):
        raise Exception('Failed to load probabilities')

    cracker = crypto.analysis.CaesarShiftCracker(alph)

    ciphertext = src.read()

    best_key = cracker.guess_key(ciphertext)

    log.write('Best key: {}'.format(best_key))

    cs = crypto.ciphers.CaesarShiftCipher(alph, best_key)

    dst.write(cs.decrypt(ciphertext))
