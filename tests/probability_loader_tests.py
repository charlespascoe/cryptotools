import unittest
import json
from crypto.alphabets import ProbabilityLoader


class ProbabilityLoaderTests(unittest.TestCase):
    def setUp(self):
        example_data = {
            'probs': [0, 0.25, 0.25, 0.5],
            'digram-probs': None,
            'trigram-probs': None
        }

        with open('tests/testing_data/example.json', 'w') as f:
            f.write(json.dumps(example_data))

        self.prob_loader = ProbabilityLoader('tests/testing_data')

    def test_nonexistant_name(self):
        self.assertIsNone(self.prob_loader.load('something'))

    def test_existant_name(self):
        result = self.prob_loader.load('example')

        self.assertEqual(result, {
            'probs': [0, 0.25, 0.25, 0.5],
            'digram-probs': None,
            'trigram-probs': None
        })
