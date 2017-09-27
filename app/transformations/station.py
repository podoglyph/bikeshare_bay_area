import pandas as pd
import datetime as dt

df = pd.read_csv('data/station.csv')

df.installation_date = pd.to_datetime(df.installation_date, format = "%m/%d/%Y").dt.date

total_docks = []

df['date'] = pd.to_datetime(df['installation_date'])

# deconstruct date for future use
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

years = df['year'].unique()
cities = df['city'].unique()

#grab some useful columns for calculation
docks = {
    'total': df.dock_count.sum(),
    'mean': df.dock_count.mean().round(2),
    'max': df.dock_count.max(),
    'min': df.dock_count.min()
}

#create individual df for each city
palo_alto = df[df.city == "Palo Alto"]
pa_total_docks_2013 = palo_alto.query('year == 2013').dock_count.sum()
pa_total_docks_2014 = palo_alto.query('year == 2014').dock_count.sum() + pa_total_docks_2013


mountain_view = df[df.city == "Mountain View"]
mv_total_docks_2013 = mountain_view.query('year == 2013').dock_count.sum()
mv_total_docks_2014 = mountain_view.query('year == 2014').dock_count.sum() + mv_total_docks_2013


redwood_city = df[df.city == "Redwood City"]
rc_total_docks_2013 = redwood_city.query('year == 2013').dock_count.sum()
rc_total_docks_2014 = redwood_city.query('year == 2014').dock_count.sum() + rc_total_docks_2013


san_francisco = df[df.city == "San Francisco"]
sf_total_docks_2013 = san_francisco.query('year == 2013').dock_count.sum()
sf_total_docks_2014 = san_francisco.query('year == 2014').dock_count.sum() + sf_total_docks_2013


san_jose = df[df.city == "San Jose"]
sj_total_docks_2013 = san_jose.query('year == 2013').dock_count.sum()
sj_total_docks_2014 = san_jose.query('year == 2014').dock_count.sum() + sj_total_docks_2013
