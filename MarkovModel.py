# NEXT STEPS

# FUTURE
# make markov model with multiple artist-albums?

import random

class MarkovModel:
  def __init__(self, text, order):
    self.text = text
    self.order = order
    self.ngrams = {}

  def check_value_exists(self, i, current_index):
    return i[current_index:current_index + self.order]

# issue with this line
  def setup_markov_list(self):
    for i in self.text:
      print(i)
      for index, value in enumerate(i):
        if (index + self.order) < len(i):
          gram = self.check_value_exists(i, index)
          if gram != None:
            # change to ' ' for full words
            gram = ''.join(gram) 
            if gram not in self.ngrams:
              self.ngrams[gram] = []
            if len(i) > self.order + index:
              self.ngrams[gram].append(i[self.order + index])
    # print(self.ngrams)
    return self.ngrams
  
  def generate_markov_model(self, string_length = 100):
    current_gram = ''.join(self.text[0][0:self.order])
    markov = current_gram
    i = 0
    # print(markov)
    while i < string_length:
      possibilities = self.ngrams[current_gram]
      next_character = random.choice((possibilities))
      markov = markov + next_character
      current_gram = markov[-self.order:]
      i = i + 1
    # print(markov)
    print("why")
    print(markov)
    return markov

  def print_ngrams(self):
    return True
    # print(self.ngrams)