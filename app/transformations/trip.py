import os
import pandas as pd
import datetime as datetime


def prep_trip_data():
    trip_path = os.path.join("data/trip.csv")
    return pd.read_csv(trip_path)

df_trip = prep_trip_data()

def transform_df_trip(data):
    data.start_date = pd.to_datetime(data.start_date, format='%m/%d/%Y %H:%M')
    data['date'] = data.start_date.dt.date

    dates = {}
    for d in data.date:
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

trips_train = transform_df_trip(df_trip)
