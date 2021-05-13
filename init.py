# NEXT STEPS
# Ask user for artist and album/song

import os
import lyricsgenius

RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

submitted_artist = input("Enter artist: ")
submitted_album = input("Enter album")

album = genius.search_album(submitted_album, submitted_artist)
album.save_lyrics()

for i in album.tracks:
    print(i.song.lyrics)


