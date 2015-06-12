import crypto.ciphers as ciphers
from crypto.alphabets import EnglishAlphabet

def create_parsers(parser):
    cipher_parser = parser.add_parser('ciphers', help='Access ciphers for encryption and decryption')
    cipher_parser.add_argument('-d', dest='decrypt', help='Decrypt', action='store_true')

    subparser = cipher_parser.add_subparsers(help='Available ciphers')

    caesar_shift_parser = subparser.add_parser('caesar-shift', help='Shifts every value forward by the shift value, modulo the length of the alphabet')
    caesar_shift_parser.add_argument('shift', type=int, help='How many positions to shift forward by')
    caesar_shift_parser.set_defaults(func=caesar_shift)

    affine_shift_parser = subparser.add_parser('affine-shift', help='(a*x + b) mod n, where x is the index of the character and n is the length of the alphabet')
    affine_shift_parser.add_argument('a', type=int, help='The value of \'a\' - must be coprime to n')
    affine_shift_parser.add_argument('b', type=int, help='The value of \'b\'')
    affine_shift_parser.set_defaults(func=affine_shift)


def handle_cipher(cipher, src, args, dst):
    f = cipher.decrypt if args.decrypt else cipher.encrypt

    dst.write(f(src.read()))


def caesar_shift(src, args, dst):
    handle_cipher(ciphers.CaesarShiftCipher(EnglishAlphabet(), args.shift), src, args, dst)


def affine_shift(src, args, dst):
    handle_cipher(ciphers.AffineShiftCipher(EnglishAlphabet(), args.a, args.b), src, args, dst)
