import crypto.alphabets
import crypto.analysis
import crypto.ciphers
import crypto.utils as utils
import os.path as op
import math

def create_parsers(parser):
    analysis_parser = parser.add_parser('analysis', help='Analysis things')

    subparsers = analysis_parser.add_subparsers(help='Analysis tools')

    caesar_shift_cracker_parser = subparsers.add_parser('caesar-shift-cracker', help='Cracks caesar shift')
    caesar_shift_cracker_parser.set_defaults(func=crack_caesar)

    affine_shift_cracker_parser = subparsers.add_parser('affine-shift-cracker', help='Cracks affine shift')
    affine_shift_cracker_parser.set_defaults(func=crack_affine)

    column_analysis_parser = subparsers.add_parser('column-analysis', help='Column Analysis')
    column_analysis_parser.set_defaults(func=column_analysis)

    vigenere_cracker_parser = subparsers.add_parser('vigenere-cracker', help='Cracks vigenere')
    vigenere_cracker_parser.add_argument('keylength', type=int, help='The length of the Vigenere Keyword')
    vigenere_cracker_parser.set_defaults(func=crack_vigenere)


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


def column_analysis(args, src, log, dst):
    pl = crypto.alphabets.ProbabilityLoader(op.join(op.dirname(op.dirname(__file__)), 'crypto/alphabets/data'))

    alph = crypto.alphabets.EnglishAlphabet()

    if not alph.init_probs(pl):
        raise Exception('Failed to load probabilities')

    src = alph.strip(src)

    if len(src) == 0:
        return

    limit = 50

    graph_width = 100

    ca = crypto.analysis.ColumnAnalyser(alph)

    iocs = ca.analyse(src, limit)

    header = (' ' * 3) + '|' + (' ' * math.floor((graph_width - 1) / 2)) + '1' + (' ' * math.floor((graph_width - 1) / 2)) + '2\n'
    header += '---|' + ('-' * graph_width) + '\n'

    log.write(header)

    alph_ioc = utils.index_of_coincidence_from_probs(alph.probs)

    for i in range(1, limit + 1):
        row = str(i).rjust(3) + '|'

        y = round(graph_width * (iocs[i] / alph_ioc) * 0.5)

        if y > graph_width:
            y = graph_width

        row += ('#' * y) + (' ' * (graph_width - y))

        log.write(row + '\n')

def crack_vigenere(args, src, log, dst):
    pl = crypto.alphabets.ProbabilityLoader(op.join(op.dirname(op.dirname(__file__)), 'crypto/alphabets/data'))

    alph = crypto.alphabets.EnglishAlphabet()

    if not alph.init_probs(pl):
        raise Exception('Failed to load probabilities')

    vc = crypto.analysis.VigenereCracker(alph)

    best_key = vc.guess_key(src, args.keylength)

    vigenere = crypto.ciphers.VigenereCipher(alph, best_key)

    plaintext = vigenere.decrypt(src)

    log.write('Best keyword: ' + best_key + '\n')
    # log.flush()

    dst.write(plaintext)
