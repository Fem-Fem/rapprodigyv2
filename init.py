# NEXT STEPS
# Ask user for artist and album/song


# INSTALLATION STEPS
# pip install jupyter
# pip3 install jupyter --user


# python -m notebook to open it

import os
import lyricsgenius
import json

# RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
# genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

# submitted_artist = input("Enter artist: ")
# submitted_album = input("Enter album: ")

# album = genius.search_album(submitted_album, submitted_artist)
# album.save_lyrics()

# for i in album.tracks:
#     print(i.song.lyrics)


with open('Lyrics_TheLostBoy.json') as f:
  data = json.load(f)

print(type(data['tracks']))