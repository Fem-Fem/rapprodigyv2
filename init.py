# NEXT STEPS
# Make plotly work better
# LOL MAKE EVERYTHING NOT RERUN IF THE FIRST CHECK FAILS

# FUTURE
# Incorporate Flask
# Incorporate NLP - Textblob?

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from Rap import Rap
from MarkovModel import MarkovModel

order = 6


def run(artist_value, album_value):
    rap = Rap()
    rap.get_credentials()
    rap.get_search_query(artist_value, album_value)
    rap.run_search_query()
    rap.open_json_file()
    rap.remove_punctuation()

    song = MarkovModel(rap.get_cleaned_rap(), order)
    song.setup_markov_list()
    return song.generate_markov_model()
    # song.print_ngrams()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Change the artist and value for some fun!"),
    html.Div(["Artist: ",
              dcc.Input(id='artist', value='Cordae', type='text')]),
    html.Br(),
    html.Div(["Album: ",
            dcc.Input(id='album', value='The Lost Boy', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='artist', component_property='value'),
    Input(component_id='album', component_property='value'),
)

def update_output_div(artist_value, album_value):
    return 'Output: {}'.format(run(artist_value, album_value))

if __name__ == '__main__':
    app.run_server(debug=True)