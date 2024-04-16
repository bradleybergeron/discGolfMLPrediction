import sqlite3

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

con = sqlite3.connect("data.db")
cur = con.cursor()

df = pd.read_sql("select p.name as playerName, t.dates, t.name as tournamentName, tp.place from tournamentPlayed tp, tournaments t, players p where t.id = tp.tournamentID and p.id = tp.playerID", con)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Disc Golf Data', style={'textAlign':'center'}),
    dcc.Dropdown(df.playerName.unique(), '', id='dropdown-player'),
    dcc.Graph(id='graph-content'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-player', 'value')
)

def update_graph(valuePlayer):
    dff = df[df.playerName==valuePlayer]
    return px.line(dff, x='tournamentName', y='place')

if __name__ == '__main__':
    app.run(debug=True)