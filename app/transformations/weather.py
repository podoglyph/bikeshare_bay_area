import os
import pandas as pd
import datetime as datetime

def run(city):
    weather = load_weather_data()
    weather = norm_precipitation_inches(weather)
    weather = norm_date(weather)
    weather = select_city(weather, city)
    events = norm_events(weather.events)
    weather = merge_events(weather, events)

    return drop_labels(weather)


def load_weather_data():
    weather_path = os.path.join("data/weather.csv")
    return pd.read_csv(weather_path)

def norm_precipitation_inches(weather):
    weather.precipitation_inches = pd.to_numeric(weather.precipitation_inches, errors = 'coerce')
    weather.loc[weather.precipitation_inches.isnull(),
        'precipitation_inches'] = weather[weather.precipitation_inches.notnull()].precipitation_inches.median()

    return weather

def norm_date(weather):
    weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')
    return weather

def select_city(weather, city):
    if city == "San Francisco":
        city_zip = 94107
    elif city == "San Jose":
        city_zip = 95113

    return weather[weather.zip_code == city_zip]

def norm_events(events):
    events.loc[events == 'rain'] = "Rain"
    events.loc[events.isnull()] = "Fair"
    return pd.get_dummies(events)

def merge_events(weather, events):
    return weather.merge(events, left_index=True, right_index=True)

def drop_labels(weather):
    weather.drop(['events', 'precipitation_inches', 'zip_code', 'max_gust_speed_mph'], axis=1, inplace=True)
    return weather


weather = run("San Francisco")

# weather.shape(733, 25)
