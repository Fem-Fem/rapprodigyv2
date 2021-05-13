# NEXT STEPS
# Ask user for artist and album/song
# Find out how to parse info that is returned

import os
import lyricsgenius

RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

artist = genius.search_artist("Cordae", max_songs=1, sort="title")
album = genius.search_album("The Lost Boy", "Cordae")
album.save_lyrics()
print(album)