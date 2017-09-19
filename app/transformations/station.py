import pandas as pd
import datetime as dt

df = pd.read_csv('data/station.csv')
df['date'] = pd.to_datetime(df['installation_date'])

# deconstruct date for future use
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df.drop(["installation_date", "date"], axis=1, inplace=True)

years = df['year'].unique()
cities = map(df['city'.unique()])

#grab some useful columns for calculation
docks = {
    'total': df.dock_count.sum(),
    'mean': df.dock_count.mean(),
    'max': df.dock_count.max(),
    'min': df.dock_count.min()
}

#create individual df for each city
palo_alto = df[df.city == "Palo Alto"]
mountain_view = df[df.city == "Mountain View"]
redwood_city = df[df.city == "Redwood City"]
san_francisco = df[df.city == "San Francisco"]
san_jose = df[df.city == "San Jose"]
