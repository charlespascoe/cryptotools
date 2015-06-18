import crypto.alphabets
import crypto.analysis
import crypto.ciphers
import os.path as op

def create_parsers(parser):
    analysis_parser = parser.add_parser('analysis', help='Analysis things')

    subparsers = analysis_parser.add_subparsers(help=   'Analysis tools')

    caesar_shift_cracker_parser = subparsers.add_parser('caesar-shift-cracker', help='Cracks caesar shift')
    caesar_shift_cracker_parser.set_defaults(func=crack_caesar)

    affine_shift_cracker_parser = subparsers.add_parser('affine-shift-cracker', help='Cracks affine shift')
    affine_shift_cracker_parser.set_defaults(func=crack_affine)


def crack_caesar(args, src, log, dst):
    pl = crypto.alphabets.ProbabilityLoader(op.join(op.dirname(op.dirname(__file__)), 'crypto/alphabets/data'))

    alph = crypto.alphabets.EnglishAlphabet()

    if not alph.init_probs(pl):
        raise Exception('Failed to load probabilities')

    cracker = crypto.analysis.CaesarShiftCracker(alph)

    ciphertext = src

    best_key = cracker.guess_key(ciphertext)

    log.write('Best key: {}'.format(best_key))

    cs = crypto.ciphers.CaesarShiftCipher(alph, best_key)

    dst.write(cs.decrypt(ciphertext))


def crack_affine(args, src, log, dst):
    pl = crypto.alphabets.ProbabilityLoader(op.join(op.dirname(op.dirname(__file__)), 'crypto/alphabets/data'))

    alph = crypto.alphabets.EnglishAlphabet()

    if not alph.init_probs(pl):
        raise Exception('Failed to load probabilities')

    cracker = crypto.analysis.AffineShiftCracker(alph)

    ciphertext = src

    best_a, best_b = cracker.guess_key(ciphertext)

    log.write('Best a: {}, Best b: {}'.format(best_a, best_b))

    afs = crypto.ciphers.AffineShiftCipher(alph, best_a, best_b)

    dst.write(afs.decrypt(ciphertext))
