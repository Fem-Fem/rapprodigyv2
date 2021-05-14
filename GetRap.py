# NEXT STEPS

# FUTURE
# Incorporate GCP

# INSTALLATION STEPS
# pip install jupyter
# pip3 install jupyter --user

# python -m notebook to open jupyter

import os
import lyricsgenius
# import code
# code.interact(local=locals())


RAP_GENIUS_ACCESS_TOKEN = os.environ.get('RAP_GENIUS_ACCESS_TOKEN')
genius = lyricsgenius.Genius(RAP_GENIUS_ACCESS_TOKEN)

# submitted_artist = input("Enter artist: ")
# submitted_album = input("Enter album: ")
submitted_artist = "Cordae"
submitted_album = "The Lost Boy"

if not os.path.exists('Lyrics_' +submitted_album.replace(" ", "")+ ".json"):
    album = genius.search_album(submitted_album, submitted_artist)
    album.save_lyrics()
