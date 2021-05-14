import unittest
from MarkovModel import MarkovModel

class TestMarkovModel(unittest.TestCase):
    def test_setup_markov_list(self):
        text = ['uh ok', "hello"]
        order = 4
        markov_dict =  {'uh o': ['k'], 'hell': ['o']}

        markov_model = MarkovModel(text, order)
        self.assertEqual(markov_model.setup_markov_list(), markov_dict)
    
    def test_generated_markov_string(self):
        text = ['uh ok', "hello"]
        order = 4
        ngrams =  {'uh o': ['k'], 'hell': ['o']}
        string_lenth = 1
        markov_model = MarkovModel(text, order)
        markov_model.ngrams = ngrams
        self.assertEqual(markov_model.generate_markov_model(string_lenth), "uh ok")

if __name__ == '__main__':
    unittest.main()