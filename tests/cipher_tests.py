import unittest
import crypto.ciphers as ciphers
from crypto.alphabets import EnglishAlphabet


class SubstitutionCipherTests(unittest.TestCase):
    def setUp(self):
        self.alph = EnglishAlphabet()
        self.key = {letter: letter for letter in self.alph}

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
            sc = ciphers.SubstitutionCipher(self.alph, 'Hello!')

    def test_invalid_key_mapping(self):
        self.key['B'] = 'A'

        result = ciphers.SubstitutionCipher.is_valid_key(self.alph, self.key)

        self.assertIsNotNone(result)
        self.assertFalse(result)

        with self.assertRaises(Exception):
            sc = ciphers.SubstitutionCipher(self.alph, self.key)

    def test_valid_key_mapping(self):
        result = ciphers.SubstitutionCipher.is_valid_key(self.alph, self.key)

        self.assertIsNotNone(result)
        self.assertTrue(result)

    def test_invert_mapping(self):
        mapping = {'A': 'X', 'B': 'Y'}

        self.assertEqual(ciphers.SubstitutionCipher.invert_mapping(mapping), {'X': 'A', 'Y': 'B'})

    def test_identity_encryption(self):
        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.encrypt('A'), 'A')

    def test_basic_encryption(self):
        self.key['A'] = 'B'
        self.key['B'] = 'A'

        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.encrypt('AABCD'), 'BBACD')

    def test_identity_decryption(self):
        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.decrypt('ABC'), 'ABC')

    def test_basic_decryption(self):
        self.key['A'] = 'B'
        self.key['B'] = 'A'

        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.decrypt('BBACD'), 'AABCD')

    def test_mixed_case_encryption(self):
        # This is specifically to test to see if it uses
        # Alpabet.strip(), as EnglishAlphabet capitalises lowercase letters

        self.key['E'] = 'O'
        self.key['O'] = 'E'

        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.encrypt('Hello, World!!'), 'HOLLEWERLD')

    def test_mixed_case_decryption(self):
        # This is specifically to test to see if it uses
        # Alpabet.strip(), as EnglishAlphabet capitalises lowercase letters

        self.key['E'] = 'O'
        self.key['O'] = 'E'

        sc = ciphers.SubstitutionCipher(self.alph, self.key)

        self.assertEqual(sc.decrypt('Holle, Werld!'), 'HELLOWORLD')


class CaesarShiftCipherTests(unittest.TestCase):
    def setUp(self):
        self.cs = ciphers.CaesarShiftCipher(EnglishAlphabet(), 0)

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
            self.cs.set_key('Hello, world!')

    def test_identity_encryption(self):
        self.assertEqual(self.cs.encrypt('A'), 'A')
        self.assertEqual(self.cs.encrypt('AABC'), 'AABC')

    def test_basic_shift_encryption(self):
        self.cs.set_key(1)
        self.assertEqual(self.cs.encrypt('A'), 'B')
        self.assertEqual(self.cs.encrypt('AABC'), 'BBCD')

    def test_modulo_encryption(self):
        self.cs.set_key(1)
        self.assertEqual(self.cs.encrypt('Z'), 'A')
        self.cs.set_key(3)
        self.assertEqual(self.cs.encrypt('XXYZ'), 'AABC')

    def test_indentity_decryption(self):
        self.assertEqual(self.cs.decrypt('A'), 'A')
        self.assertEqual(self.cs.decrypt('AABC'), 'AABC')

    def test_basic_shift_decryption(self):
        self.cs.set_key(1)
        self.assertEqual(self.cs.decrypt('B'), 'A')
        self.assertEqual(self.cs.decrypt('BBCD'), 'AABC')

    def test_modulo_decryption(self):
        self.cs.set_key(1)
        self.assertEqual(self.cs.decrypt('A'), 'Z')
        self.cs.set_key(3)
        self.assertEqual(self.cs.decrypt('AABC'), 'XXYZ')


class AffineShiftCipherTests(unittest.TestCase):
    def setUp(self):
        self.afs = ciphers.AffineShiftCipher(EnglishAlphabet(), 1, 0)

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
            self.afs.set_key('A', 'B')

    def test_invalid_key_value(self):
        with self.assertRaises(Exception):
            self.afs.set_key(2, 0)

    def test_identity_encryption(self):
        self.assertEqual(self.afs.encrypt('A'), 'A')
        self.assertEqual(self.afs.encrypt('AABC'), 'AABC')

    def test_basic_a_key_encryption(self):
        self.afs.set_key(3, 0)
        self.assertEqual(self.afs.encrypt('ABBC'), 'ADDG')

    def test_basic_b_key_encryption(self):
        self.afs.set_key(1, 1)
        self.assertEqual(self.afs.encrypt('ABBC'), 'BCCD')

    def test_basic_key_encryption(self):
        self.afs.set_key(3, 2)
        self.assertEqual(self.afs.encrypt('AABBCC'), 'CCFFII')
