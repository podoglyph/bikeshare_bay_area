import os
import pandas as pd
import datetime as datetime


def run():
    df = prep_trip_data()
    trips_per_day = transform_trips(df)
    return trips_per_day

def prep_trip_data():
    trip_path = os.path.join("data/trip.csv")
    return pd.read_csv(trip_path)

def transform_trips(df):
    df.start_date = pd.to_datetime(df.start_date, format='%m/%d/%Y %H:%M')
    df['date'] = df.start_date.dt.date

    dates = {}
    for d in df.date:
        if d not in dates:
            dates[d] = 1
        else:
            dates[d] += 1

    df = pd.DataFrame.from_dict(dates, orient = "index")
    df['date'] = df.index
    df['trips'] = df.iloc[:,0]
    trips_train = df.iloc[:,1:3]
    trips_train = trips_train.sort_values('date')
    trips_train.reset_index(drop=True, inplace=True)
    return trips_train

trips_per_day = run()

# (733, 2)
