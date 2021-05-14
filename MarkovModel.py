# NEXT STEPS
# make markov model

# FUTURE
# make markov model with multiple artist-albums?

class MarkovModel:
  def __init__(self, text, order):
    self.text = text
    self.order = order
    self.ngrams = {}

  def check_value_exist(self, i, current_index):
    return i[current_index:current_index + self.order]

  def setup_markov_list(self):
    for i in self.text:
      for index, value in enumerate(i):
        if (index + self.order - 1) < len(i):
          gram = self.check_value_exist(i, index)
          if gram != None:
            gram = ' '.join(gram) 
            if gram in self.ngrams :
              self.ngrams[gram] = self.ngrams[gram] + 1
            else:
              self.ngrams[gram] = 1

  def print_ngrams(self):
    print(self.ngrams)