# NEXT STEPS
# Store values somehow

# FUTURE
import json
import re


with open('Lyrics_TheLostBoy.json') as f:
  data = json.load(f)

for i in data['tracks']:
    string_being_cleaned = i['song']['lyrics']
    number_of_question_marks = string_being_cleaned.count('?')
    string_being_cleaned = re.sub('[.,?]', "", string_being_cleaned)
    string_being_cleaned = re.sub('[\n]', " ", string_being_cleaned)
    string_being_cleaned = re.sub('\[.+?\]\s', '', string_being_cleaned)
    string_being_cleaned = string_being_cleaned.lower()

    # print(i['song']['lyrics'].translate(str.maketrans({'\n': ' ', ',': '', '.': ''})).lower())