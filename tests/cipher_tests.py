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

class CaesarShiftTests(unittest.TestCase):
    def setUp(self):
        self.cs = ciphers.CaesarShift(EnglishAlphabet())

    def test_identity_encryption(self):
        self.assertEqual(self.cs.encrypt(0, 'A'), 'A')
        self.assertEqual(self.cs.encrypt(0, 'AABC'), 'AABC')

    def test_basic_shift_encryption(self):
        self.assertEqual(self.cs.encrypt(1, 'A'), 'B')
        self.assertEqual(self.cs.encrypt(1, 'AABC'), 'BBCD')

    def test_modulo_encryption(self):
        self.assertEqual(self.cs.encrypt(1, 'Z'), 'A')
        self.assertEqual(self.cs.encrypt(3, 'XXYZ'), 'AABC')

    def test_indentity_decryption(self):
        self.assertEqual(self.cs.decrypt(0, 'A'), 'A')
        self.assertEqual(self.cs.decrypt(0, 'AABC'), 'AABC')

    def test_basic_shift_decryption(self):
        self.assertEqual(self.cs.decrypt(1, 'B'), 'A')
        self.assertEqual(self.cs.decrypt(1, 'BBCD'), 'AABC')

    def test_modulo_decryption(self):
        self.assertEqual(self.cs.decrypt(1, 'A'), 'Z')
        self.assertEqual(self.cs.decrypt(3, 'AABC'), 'XXYZ')


class AffineShiftTests(unittest.TestCase):
    def setUp(self):
        self.afs = ciphers.AffineShift(EnglishAlphabet())

    def test_invalid_key_value(self):
        with self.assertRaises(Exception):
            self.afs.encrypt(2, 0, 'Test')

    def test_identity_encryption(self):
        self.assertEqual(self.afs.encrypt(1, 0, 'A'), 'A')
        self.assertEqual(self.afs.encrypt(1, 0, 'AABC'), 'AABC')

    def test_basic_a_key_encryption(self):
        self.assertEqual(self.afs.encrypt(3, 0, 'ABBC'), 'ADDG')

    def test_basic_b_key_encryption(self):
        self.assertEqual(self.afs.encrypt(1, 1, 'ABBC'), 'BCCD')

    def test_basic_key_encryption(self):
        self.assertEqual(self.afs.encrypt(3, 2, 'AABBCC'), 'CCFFII')
