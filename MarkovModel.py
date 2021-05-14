# NEXT STEPS
# make markov model

# FUTURE
# make markov model with multiple artist-albums?

text = "Spit hot lava erode the beat"
text = ["Spit", "hot", "lava", "erode", "the", "beat"]
ngrams = {}
order = 3

def check_value_exist(text, current_index, order):
  return text[current_index:current_index + order]

  # if (current_index + order - 1) < len(text):
  #   return text[current_index:current_index + order]
  # else:
  #   return None

for index, value in enumerate(text):
  if (index + order - 1) < len(text):
    gram = check_value_exist(text, index, order)
    if gram != None:
      gram = ' '.join(gram) 
      if gram in ngrams :
        ngrams[gram] = ngrams[gram] + 1
      else:
        ngrams[gram] = 1
    print(gram)

print(ngrams)
