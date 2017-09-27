import os
import pandas as pd
import datetime as datetime

def load_weather_data():
    weather_path = os.path.join("data/weather.csv")
    return pd.read_csv(weather_path)

weather = load_weather_data()

weather.precipitation_inches = pd.to_numeric(weather.precipitation_inches, errors = 'coerce')

weather.loc[weather.events == 'rain', 'events'] = "Rain"
weather.loc[weather.events.isnull(), 'events'] = "Normal"
events = pd.get_dummies(weather.events)

weather.date = pd.to_datetime(weather.date, format='%m/%d/%Y')
weather = weather[weather.zip_code == 95113]
weather = weather.drop("zip_code", 1)
weather_train = weather.merge(events, left_index=True, right_index=True)
weather_train = weather_train.drop("max_gust_speed_mph", 1)

weather_train.precipitation_inches = pd.to_numeric(weather_train.precipitation_inches, errors = 'coerce')

weather_train.loc[weather_train.precipitation_inches.isnull(),
            'precipitation_inches'] = weather_train[weather_train.precipitation_inches.notnull()].precipitation_inches.median()


weather_train.drop(["events", "precipitation_inches"], 1, inplace=True)
