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

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div(className='container', children=[
    html.H1(children='Bike Dash'),

    html.Div(children='''
        Bike Share SF: Data Insight into Bike Trips.
    '''),

    html.Div([
        html.H2("Bay Area Dock Stats", style={'color': 'blue'}),
        html.Ul([
            html.Li([
                html.Div([
                    html.H6('Total Docks', style={'position': 'relative', 'bottom': '45px'}),
                    html.Span(docks['total'], style={'position': 'relative', 'bottom': '8px', 'color': '#fff', 'font-size': '24px'})
                ], style={'position': 'relative', 'border': '1px solid #000', 'border-radius': '50%', 'width': '115px', 'height': '115px', 'margin': '0 auto', 'background-color': '#36E666'})

            ], className='dock_count three columns', id='dc-1', style={}),

            html.Li([
                html.Div([
                    html.H6('Mean', style={'position': 'relative', 'bottom': '45px'}),
                    html.Span(docks['mean'], style={'position': 'relative', 'bottom': '8px', 'color': '#fff', 'font-size': '24px'})
                ], style={'position': 'relative', 'border': '1px solid #000', 'border-radius': '50%', 'width': '115px', 'height': '115px', 'margin': '0 auto', 'background-color': '#36E666'})
            ], className='dock_count three columns', id='dc-2', style={}),

            html.Li([
                html.Div([
                    html.H6('Max', style={'position': 'relative', 'bottom': '45px'}),
                    html.Span(docks['max'], style={'position': 'relative', 'bottom': '8px', 'color': '#fff', 'font-size': '24px'})
                ], style={'position': 'relative', 'border': '1px solid #000', 'border-radius': '50%', 'width': '115px', 'height': '115px', 'margin': '0 auto', 'background-color': '#36E666'})
            ], className='dock_count three columns', id='dc-3', style={}),

            html.Li([
                html.Div([
                    html.H6('Min', style={'position': 'relative', 'bottom': '45px'}),
                    html.Span(docks['min'], style={'position': 'relative', 'bottom': '8px', 'color': '#fff', 'font-size': '24px'})
                ], style={'position': 'relative', 'border': '1px solid #000', 'border-radius': '50%', 'width': '115px', 'height': '115px', 'margin': '0 auto', 'background-color': '#36E666'})
            ], className='dock_count three columns', id='dc-4', style={})
        ], style={'list-style': 'none', 'margin-top': '50px'}),

    ], className='row', style={'margin': '0 auto', 'text-align': 'center'}),

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
