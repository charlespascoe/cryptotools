import unittest
import crypto.utils as utils
from crypto.alphabets import EnglishAlphabet


class GCDTests(unittest.TestCase):
    def test_coprime_values(self):
        self.assertEqual(utils.gcd(4, 9), 1)
        self.assertEqual(utils.gcd(17, 26), 1)
        self.assertEqual(utils.gcd(124, 121), 1)

    def test_non_coprime_values(self):
        self.assertEqual(utils.gcd(6, 8), 2)
        self.assertEqual(utils.gcd(12, 15), 3)
        self.assertEqual(utils.gcd(100, 300), 100)
        self.assertEqual(utils.gcd(0, 100), 100)

class ComputeCoprimesTests(unittest.TestCase):
    def test_prime_values(self):
        self.assertEqual(utils.compute_coprimes(7), [i for i in range(1, 7)])
        self.assertEqual(utils.compute_coprimes(31), [i for i in range(1, 31)])
        self.assertEqual(utils.compute_coprimes(97), [i for i in range(1, 97)])

    def test_composite_values(self):
        self.assertEqual(utils.compute_coprimes(15), [1, 2, 4, 7, 8, 11, 13, 14])
        self.assertEqual(utils.compute_coprimes(30), [1, 7, 11, 13, 17, 19, 23, 29])


class PhiTests(unittest.TestCase):
    def test_prime_values(self):
        examples = [
            (7, 6),
            (31, 30),
            (17, 16),
            (733, 732),
            (503, 502),
            (991, 990)
        ]

        for x, y in examples:
            self.assertEqual(utils.phi(x), y)

    def test_composite_values(self):
        examples = [
            (15, 8),
            (30, 8),
            (100, 40),
            (1024, 512)
        ]

        for x, y in examples:
            self.assertEqual(utils.phi(x), y)


class ComputeInverseTests(unittest.TestCase):
    def test_valid_values(self):
        examples = [
            (2, 7, 4),
            (21, 31, 3),
            (12, 13, 12)
        ]

        for x, n, inv in examples:
            self.assertEqual(utils.compute_inverse(x, n), inv)

    def test_invalid_values(self):
        examples = [
            (2, 4),
            (13, 26),
            (60, 100)
        ]

        for x, n in examples:
            self.assertIsNone(utils.compute_inverse(x, n))


class ComputeFrequenciesTests(unittest.TestCase):
    def setUp(self):
        self.alph = EnglishAlphabet()

    def test_simple_string(self):
        freqs = utils.compute_frequencies('AAABBCD', self.alph)
        self.assertEqual(freqs, [3, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_complex_string(self):
        freqs = utils.compute_frequencies('Hello, World!!!', self.alph)
        self.assertEqual(freqs, [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0])


class ComputePropbabilitiesTests(unittest.TestCase):
    def setUp(self):
        self.alph = EnglishAlphabet()

    def test_empty_string(self):
        probs = utils.compute_probabilities('', self.alph)
        self.assertEqual(probs, [0] * len(self.alph))

    def test_simple_string(self):
        probs = utils.compute_probabilities('AAABBCD', self.alph)
        self.assertEqual(probs, [3/7, 2/7, 1/7, 1/7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_complex_string(self):
        probs = utils.compute_probabilities('Hello, World!!!', self.alph)
        self.assertEqual(probs, [0, 0, 0, 1/10, 1/10, 0, 0, 1/10, 0, 0, 0, 3/10, 0, 0, 2/10, 0, 0, 1/10, 0, 0, 0, 0, 1/10, 0, 0, 0])
