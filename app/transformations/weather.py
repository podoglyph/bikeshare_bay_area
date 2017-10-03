import os
import pandas as pd
import datetime as datetime

def run(city):
    weather = load_weather_data()
    weather = norm_precipitation_inches(weather)
    weather = norm_date(weather)
    weather = select_city(city)
    events = norm_events(weather.events)
    weather = merge_events(weather, events)

    return drop_labels(weather)


#private
def load_weather_data():
    weather_path = os.path.join("data/weather.csv")
    return pd.read_csv(weather_path)

def norm_precipitation_inches(weather):
    weather.loc[weather.precipitation_inches.isnull(),
        'precipitation_inches'] = weather[weather.precipitation_inches.notnull()].precipitation_inches.median()
        
    return weather.precipitation_inches = pd.to_numeric(weather.precipitation_inches, errors = 'coerce')

def norm_date(weather):
    return weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')

def select_city(city):
    if city == "San Francisco":
        city_zip = 94107
    else city == "San Jose":
        city_zip = 95113

    return weather[weather.zip_code == city_zip]

def norm_events(events):
    events.loc[events == 'rain'] = "Rain"
    events.loc[events.isnull()] = "Fair"
    return pd.get_dummies(events)

def merge_events(weather, events):
    return weather.merge(events, left_index=True, right_index=True)

def drop_labels(weather):
    weather.drop(['events'], axis=1)
    weather = weather.drop("zip_code", 1)
    return weather





weather_train.drop(["events", "precipitation_inches"], 1, inplace=True)

weather = run("San Francisco")
