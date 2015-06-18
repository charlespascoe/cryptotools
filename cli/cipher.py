import crypto.ciphers as ciphers
from crypto.alphabets import EnglishAlphabet

def create_parsers(parser):
    cipher_parser = parser.add_parser('ciphers', help='Access ciphers for encryption and decryption')
    cipher_parser.add_argument('-d', dest='decrypt', help='Decrypt', action='store_true')

    subparsers = cipher_parser.add_subparsers(help='Available ciphers')

    caesar_shift_parser = subparsers.add_parser('caesar-shift', help='Shifts every value forward by the shift value, modulo the length of the alphabet')
    caesar_shift_parser.add_argument('shift', type=int, help='How many positions to shift forward by')
    caesar_shift_parser.set_defaults(func=caesar_shift)

    affine_shift_parser = subparsers.add_parser('affine-shift', help='(a*x + b) mod n, where x is the index of the character and n is the length of the alphabet')
    affine_shift_parser.add_argument('a', type=int, help='The value of \'a\' - must be coprime to n')
    affine_shift_parser.add_argument('b', type=int, help='The value of \'b\'')
    affine_shift_parser.set_defaults(func=affine_shift)

    vigenere_parser = subparsers.add_parser('vigenere', help='A simple Polyalphabetic cipher')
    vigenere_parser.add_argument('keyword', help='The keyword used to encrypt the text')
    vigenere_parser.set_defaults(func=vigenere)


def handle_cipher(cipher, args, src, log, dst):
    f = cipher.decrypt if args.decrypt else cipher.encrypt

    dst.write(f(src))


def caesar_shift(args, src, log, dst):
    handle_cipher(ciphers.CaesarShiftCipher(EnglishAlphabet(), args.shift), args, src, log, dst)


def affine_shift(args, src, log, dst):
    handle_cipher(ciphers.AffineShiftCipher(EnglishAlphabet(), args.a, args.b), args, src, log, dst)


def vigenere(args, src, log, dst):
    handle_cipher(ciphers.VigenereCipher(EnglishAlphabet(), args.keyword), args, src, log, dst)
