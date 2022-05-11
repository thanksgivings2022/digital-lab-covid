from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

from layouts import *
import callbacks
from components import navbar

app = Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home
    elif pathname == '/exploration':
        return layout1
    elif pathname == '/prediction':
        return layout3
    else:
        return html.Div([navbar.navbar(),"404"])


if __name__ == '__main__':
    app.run_server(debug=True)
