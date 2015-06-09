import unittest
import crypto.alphabets
import string

class AlphabetTests(unittest.TestCase):
    def setUp(self):
        self.alph = crypto.alphabets.Alphabet()
        self.alph._alph = string.ascii_uppercase

    def test_indexing(self):
        self.assertEqual(self.alph[0], 'A')
        self.assertEqual(self.alph[25], 'Z')

    def test_inverse_index(self):
        self.assertEqual(self.alph.index('A'), 0)
        self.assertEqual(self.alph.index('Z'), 25)

    def test_len(self):
        self.assertEqual(len(self.alph), 26)

    def test_strip(self):
        self.assertEqual(self.alph.strip('AbCdEf123'), 'ACE')

    def test_iter(self):
        s = ''.join([letter for letter in self.alph])

        self.assertEqual(s, string.ascii_uppercase)

    def test_str(self):
        self.assertEqual(str(self.alph), string.ascii_uppercase)

    def test_contains(self):
        self.assertTrue('A' in self.alph)
        self.assertFalse('a' in self.alph)
        self.assertFalse('1' in self.alph)
