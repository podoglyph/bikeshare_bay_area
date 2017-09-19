# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import datetime as dt
import pandas as pd
import pdb
import json

# data_dict = [
#     {'x': [2013, 2014, 2015], 'y': [2, 5, 10], 'type': 'bar', 'name': 'San Francisco'},
#     {'x': [2013, 2014, 2015], 'y': [9, 6, 14], 'type': 'bar', 'name': 'San Jose'},
#     {'x': [2013, 2014, 2015], 'y': [9, 4, 19], 'type': 'bar', 'name': 'Palo Alto'},
#     {'x': [2013, 2014, 2015], 'y': [4, 9, 16], 'type': 'bar', 'name': 'Mountain View'},
#     {'x': [2013, 2014, 2015], 'y': [6, 6, 12], 'type': 'bar', 'name': 'Redwood City'},
# ]


df = pd.read_csv('data/station.csv')
df['date'] = pd.to_datetime(df['installation_date'])

# deconstruct date for future use
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

#drop extra date columns
df.drop(["installation_date", "date"], axis=1, inplace=True)

#grab some useful columns for calculation
docks = {
    'total': df.dock_count.sum(),
    'mean': df.dock_count.mean(),
    'max': df.dock_count.max(),
    'min': df.dock_count.min()
}

app = dash.Dash()

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

    html.Label('Radio Items'),
    dcc.RadioItems(
        id='radio-city',
        options=[
            {'label': 'San Francisco', 'value': 'San Francisco'},
            {'label': 'San Jose', 'value': 'San Jose'},
            {'label': 'Redwood City', 'value': 'Redwood City'},
            {'label': 'Mountain View', 'value': 'Mountain View'},
            {'label': 'Palo Alto', 'value': 'Palo Alto'}
        ],
        value='San Francisco'
    ),

    dcc.Graph(
        id='stations',
        figure={
            'data': [
                {
                    'x': df.city.unique(),
                    'y': df.dock_count,
                    'name': 'Docks by City',
                }
            ],
            'layout': {
                'title': 'Trips per Day Visualization'
            }
        }
    )

])

@app.callback(dash.dependencies.Output('stations', 'figure'),
          [dash.dependencies.Input('radio-city', 'value')])
def update_figure(selected_city):
    # print(selected_city) #func param necessary. prints to terminal.
    filtered_df = df[df.city == selected_city]

    test_me = {
        'data': [
            {
                'x': selected_city,
                'y': df.dock_count,
                'name': 'Docks by City',
            }
        ]
    }

    print(test_me)

if __name__ == '__main__':
    app.run_server(debug=True)
