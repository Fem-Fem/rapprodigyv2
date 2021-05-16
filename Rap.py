# NEXT STEPS
# Store values in SQL
# Artist - Album - - Lyrics

# FUTURE
# Length of words
# question marks
# words per album
# most common words
# number of unique words

# INSTALLATION STEPS
# pip install jupyter
# pip3 install jupyter --user
# pip install plotly==4.14.3
# pip install dash --user
# pip install lyricsgenius
# pip install gunicorn

# pywin32==300

# python -m notebook to open jupyter

import os
import lyricsgenius
import json
import re
# from boto.s3.connection import S3Connection


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
    ### EDIT THIS FOR HEROKU - ADD ACCESS TOKEN
    # RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
    # genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

    # s3 = S3Connection(os.environ['RAP_GENIUS_ACCESS_TOKEN'])

    RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
    genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

    self.genius = genius

  def get_search_query(self, artist="Cordae", album="The Lost Boy"):
    self.artist = artist
    self.album = album
    self.directory = 'Lyrics_' +album.replace(" ", "")+ ".json"

  def run_search_query(self):
    print(self.directory)
    if not os.path.exists(self.directory):
      album = self.genius.search_album(self.album, self.artist)
      if album == None:
        return False
      album.save_lyrics()
    return True

  def open_json_file(self):
    with open(self.directory) as f:
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