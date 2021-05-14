# NEXT STEPS
# Store values in GCP
# Artist - Album - Song Name - Lyrics

# FUTURE

# INSTALLATION STEPS
# pip install jupyter
# pip3 install jupyter --user
# pip install plotly==4.14.3
# pip install dash --user

# python -m notebook to open jupyter

import os
import lyricsgenius
import json
import re

# import code
# code.interact(local=locals())

class Rap:
  def __init__(self):
    self.data = ''
    self.cleaned_album_lyrics = []
    self.number_of_question_marks = 0
    self.directory = ''
    self.cleaned_album_lyrics = []

  def get_credentials(self):
    RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
    genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

  def get_search_query(self):
    # submitted_artist = input("Enter artist: ")
    # submitted_album = input("Enter album: ")
    submitted_artist = "Cordae"
    submitted_album = "The Lost Boy"
    self.artist = submitted_artist
    self.album = submitted_album
    self.directory = 'Lyrics_' +submitted_album.replace(" ", "")+ ".json"

  def run_search_query(self):
    if not os.path.exists(self.directory):
      album = genius.search_album(submitted_album, submitted_artist)
      album.save_lyrics()

  def open_json_file(self):
    with open('Lyrics_TheLostBoy.json') as f:
      self.data = json.load(f)

  def remove_punctuation(self):    
    for i in self.data['tracks']:
      song_track_lyrics_being_cleaned = i['song']['lyrics']
      self.number_of_question_marks = song_track_lyrics_being_cleaned.count('?')
      
      song_track_lyrics_being_cleaned = re.sub('[.,?"\']', "", song_track_lyrics_being_cleaned)
      song_track_lyrics_being_cleaned = re.sub('[\n]', " ", song_track_lyrics_being_cleaned)
      song_track_lyrics_being_cleaned = re.sub('\[.+?\]\s', '', song_track_lyrics_being_cleaned)
      song_track_lyrics_being_cleaned = song_track_lyrics_being_cleaned.lower()
      self.cleaned_album_lyrics.append(song_track_lyrics_being_cleaned)
  
  # uncomment for full words
  # def remove_spaces(self):
  #   self.cleaned_album_lyrics = [i.split(" ") for i in self.cleaned_album_lyrics]

  def get_cleaned_rap(self):
    return self.cleaned_album_lyrics