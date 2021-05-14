# NEXT STEPS

# FUTURE
# Incorporate Flask
# Incorporate Plotly
# Add unit tests
# Incorporate NLP

import json
import re
from Rap import Rap
from MarkovModel import MarkovModel

order = 3

rap = Rap()
rap.get_credentials()
rap.get_search_query()
rap.run_search_query()
rap.open_json_file()
rap.remove_punctuation()
rap.remove_spaces()

song = MarkovModel(rap.get_cleaned_rap(), order)
song.setup_markov_list()
song.print_ngrams()