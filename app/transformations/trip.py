import os
import pandas as pd
import datetime as datetime


def prep_trip_data():
    trip_path = os.path.join("data/trip.csv")
    return pd.read_csv(trip_path)

df_trip = prep_trip_data()

def transform_df_trip(data):
    # data.dropna(axis=0, how='any', inplace=True)
    data['duration'] /= 60
    data.start_date = pd.to_datetime(data.start_date, format='%m/%d/%Y %H:%M')
    data['date'] = data.start_date.dt.date
    # data.drop(["start_station_name", "end_date", "bike_id", "subscription_type", "start_station_id", "end_station_name", "end_station_id"], 1, inplace=True)

    dates = {}
    for d in data.date:
        if d not in dates:
            dates[d] = 1
        else:
            dates[d] += 1

    dates

    data.drop("start_date", 1, inplace=True)
    df = pd.DataFrame.from_dict(dates, orient = "index")
    df['date'] = df.index
    df['trips'] = df.iloc[:,0]
    trips_train = df.iloc[:,1:3]
    trips_train.reset_index(drop = True, inplace = True)
    trips_train = trips_train.sort_values('date')
    trips_train.reset_index(drop=True, inplace=True)
    return trips_train

trips_train = transform_df_trip(df_trip)
# this returns:
#            date  trips
# 0    2013-08-29    748
# 1    2013-08-30    714
# 2    2013-08-31    640
# 3    2013-09-01    706


# trips_per_day = {}
# trips_per_day = transformed_trip.to_dict(orient="list")
