# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import pdb
import pandas as pd

df = pd.read_csv('data/station.csv')
df['date'] = pd.to_datetime(df['installation_date'])

# deconstruct date for future use
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

def get_years():
    return df['year'].unique()

def get_cities():
    return map(df['city'.unique()])
#drop extra date columns
df.drop(["installation_date", "date"], axis=1, inplace=True)

#grab some useful columns for calculation
docks = {
    'total': df.dock_count.sum(),
    'mean': df.dock_count.mean(),
    'max': df.dock_count.max(),
    'min': df.dock_count.min()
}

palo_alto = df[df.city == "Palo Alto"]
mountain_view = df[df.city == "Mountain View"]
redwood_city = df[df.city == "Redwood City"]
san_francisco = df[df.city == "San Francisco"]
san_jose = df[df.city == "San Jose"]


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

    dcc.Graph(
        id='docks_per_year',
        figure={
            'data': [
                {'x': get_years(), 'y': [22, 33], 'type': 'bar', 'name': 'Palo Alto'},
                {'x': get_years(), 'y': [23, 43], 'type': 'bar', 'name': 'Mountain View'},
                {'x': get_years(), 'y': [24, 54], 'type': 'bar', 'name': 'San Francisco'},
                {'x': get_years(), 'y': [25, 55], 'type': 'bar', 'name': 'San Jose'},
                {'x': get_years(), 'y': [26, 57], 'type': 'bar', 'name': 'Redwood City'},
            ],
            'layout': {
                'title': 'City Docks per Year'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
