# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pdb
import pandas as pd
from transformations import station

docks = station.docks
years = station.years

app = dash.Dash()
# b
app.layout = html.Div(children=[
    html.H1(children='Bike Dash'),

    html.Div(children='''
        Bike Share SF: Data Insight into Bike Trips.
    '''),

    html.Div([
        html.H1("Bay Area Dock Stats", style={'color': 'blue', 'fontSize': 12}),

        html.P('Total Docks: %s' % docks['total'], className='dock_count', id='dc-1'),
        html.P('Mean: %s' % docks['mean'], className='dock_count', id='dc-2'),
        html.P('Max: %s' % docks['max'], className='dock_count', id='dc-3'),
        html.P('Min: %s' % docks['min'], className='dock_count', id='dc-4')
    ], style={'marginBottom': 10, 'marginTop': 15}),

    dcc.Graph(
        id='docks_per_year',
        figure={
            'data': [
                {'x': years, 'y': [22, 33], 'type': 'bar', 'name': 'Palo Alto'},
                {'x': years, 'y': [23, 43], 'type': 'bar', 'name': 'Mountain View'},
                {'x': years, 'y': [24, 54], 'type': 'bar', 'name': 'San Francisco'},
                {'x': years, 'y': [25, 55], 'type': 'bar', 'name': 'San Jose'},
                {'x': years, 'y': [26, 57], 'type': 'bar', 'name': 'Redwood City'},
            ],
            'layout': {
                'title': 'City Docks per Year'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
