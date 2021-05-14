# NEXT STEPS
# Store values somehow

# FUTURE
import json
import re


with open('Lyrics_TheLostBoy.json') as f:
  data = json.load(f)

cleaned_album_lyrics = []

for i in data['tracks']:
    song_track_lyrics_being_cleaned = i['song']['lyrics']
    number_of_question_marks = song_track_lyrics_being_cleaned.count('?')
    song_track_lyrics_being_cleaned = re.sub('[.,?]', "", song_track_lyrics_being_cleaned)
    song_track_lyrics_being_cleaned = re.sub('[\n]', " ", song_track_lyrics_being_cleaned)
    song_track_lyrics_being_cleaned = re.sub('\[.+?\]\s', '', song_track_lyrics_being_cleaned)
    song_track_lyrics_being_cleaned = song_track_lyrics_being_cleaned.lower()
    cleaned_album_lyrics.append(song_track_lyrics_being_cleaned)

for i in cleaned_album_lyrics:
    lyrics = i.split(" ")
    print(string)
    for i in string
    # print(i['song']['lyrics'].translate(str.maketrans({'\n': ' ', ',': '', '.': ''})).lower())