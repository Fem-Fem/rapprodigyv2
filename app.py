# NEXT STEPS
# LOL MAKE EVERYTHING NOT RERUN IF THE FIRST CHECK FAILS

# FUTURE
# Incorporate NLP - Textblob?
# Chart of words?
# Compare two rappers to each other?

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from Rap import Rap
from MarkovModel import MarkovModel

order = 6

def run(artist_value, album_value):
    rap = Rap()
    rap.get_credentials()
    rap.get_search_query(artist_value, album_value)
    valid_search_query = rap.run_search_query()
    if valid_search_query:
        rap.open_json_file()
        rap.remove_punctuation()

        song = MarkovModel(rap.get_cleaned_rap(), order)
        song.setup_markov_list()
        return song.generate_markov_model()
    return "Invalid!"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H6("Change the artist and value for some fun!"),
    html.Div(["Artist: ",
              dcc.Input(id='artist', value='Cordae', type='text', debounce=True)]),
    html.Br(),
    html.Div(["Album: ",
            dcc.Input(id='album', value='The Lost Boy', type='text', debounce=True)]),
    html.Br(),
    html.Button(id='submit', type='submit', children='Submit', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='artist', component_property='value'), 
    State(component_id='album', component_property='value')]
)

def update_output_div(submit, artist_value, album_value):
    print(submit)
    print(artist_value)
    print(album_value)
    # return "hi"
    return 'Output: {}'.format(run(artist_value, album_value))

if __name__ == '__main__':
    app.run_server(debug=True)