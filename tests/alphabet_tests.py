import unittest
import crypto.alphabets
import string
import json


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


class AlphetbetWithProbabilitiesTests(unittest.TestCase):
    def setUp(self):
        self.alph = crypto.alphabets.EnglishAlphabet()

        data = {
            'probs': [1/26 for i in range(len(self.alph))],
            'digram-probs': None,
            'trigram-probs': None
        }

        with open('tests/testing_data/' + self.alph.__class__.__name__ + '.json', 'w') as f:
            f.write(json.dumps(data))

        self.prob_loader = crypto.alphabets.ProbabilityLoader('tests/testing_data/')

    def test_no_data(self):
        p = crypto.alphabets.ProbabilityLoader('tests/')

        self.assertFalse(self.alph.init_probs(p))

        with self.assertRaises(Exception):
            self.alph.prob(alph[0])

    def test_with_data(self):
        self.assertTrue(self.alph.init_probs(self.prob_loader))

        for letter in self.alph:
            self.assertEqual(self.alph.prob(letter), 1/26)
