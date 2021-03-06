# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pdb
import pandas as pd
from transformations import station
from styles import custom_styles

docks = station.docks
years = station.years

# Custom styles because you can't use an internal stylesheet in Dash.
round_icon = custom_styles.round_icon
round_title = custom_styles.round_title
round_value = custom_styles.round_value
round_row = custom_styles.round_row

app = dash.Dash()

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div(className='container', children=[
    html.H1(children='Bike Dash'),

    html.Div(children='''
        Bike Share SF: Data Insight into Bike Trips.
    '''),

    html.Div([
        html.H2("Bay Area Dock Stats", style={}),
        html.Ul([
            html.Li([
                html.Div([
                    html.H6('Total Docks', style=round_title),
                    html.Span(docks['total'], style=round_value)
                ], style=round_icon)

            ], className='dock_count three columns'),

            html.Li([
                html.Div([
                    html.H6('Mean', style=round_title),
                    html.Span(docks['mean'], style=round_value)
                ], style=round_icon)
            ], className='dock_count three columns'),

            html.Li([
                html.Div([
                    html.H6('Max', style=round_title),
                    html.Span(docks['max'], style=round_value)
                ], style=round_icon)
            ], className='dock_count three columns'),

            html.Li([
                html.Div([
                    html.H6('Min', style=round_title),
                    html.Span(docks['min'], style=round_value)
                ], style=round_icon)
            ], className='dock_count three columns')
        ], style={'list-style': 'none', 'margin-top': '50px'}),

    ], className='row', style=round_row),

    # Need to make this more dynamic. Form a list of dictionaries.
    dcc.Graph(
        id='docks_per_year',
        figure={
            'data': [
                {'x': years, 'y': [station.pa_total_docks_2013, station.pa_total_docks_2014], 'type': 'bar', 'name': 'Palo Alto'},
                {'x': years, 'y': [station.mv_total_docks_2013, station.mv_total_docks_2014], 'type': 'bar', 'name': 'Mountain View'},
                {'x': years, 'y': [station.sf_total_docks_2013, station.sf_total_docks_2014], 'type': 'bar', 'name': 'San Francisco'},
                {'x': years, 'y': [station.sj_total_docks_2013, station.sj_total_docks_2014], 'type': 'bar', 'name': 'San Jose'},
                {'x': years, 'y': [station.rc_total_docks_2013, station.rc_total_docks_2014], 'type': 'bar', 'name': 'Redwood City'},
            ],
            'layout': {
                'title': 'City Docks per Year'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
