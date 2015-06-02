import unittest
import crypto.alphabets
import string

class AlphabetTests(unittest.TestCase):
    def setUp(self):
        self.alph = crypto.alphabets.Alphabet()
        self.alph = string.ascii_uppercase

    def test_indexing(self):
        self.assertEqual(self.alph[0], 'A')
        self.assertEqual(self.alph[25], 'Z')

    def test_inverse_index(self):
        self.assertEqual(self.alph.index('A'), 0)
        self.assertEqual(self.alph.index('Z'), 25)

    def test_len(self):
        self.assertEqual(len(self.alph), 26)