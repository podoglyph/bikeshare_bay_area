import pandas as pd
import datetime as dt

df = pd.read_csv('data/station.csv')
df['date'] = pd.to_datetime(df['installation_date'])

# deconstruct date for future use
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

years = df['year'].unique()

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
