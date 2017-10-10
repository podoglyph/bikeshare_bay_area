from transformations import weather, trip

df_weather = weather.weather
df_trip = trip.trips_per_day

train = df_weather.merge(df_trip, on = df_weather.date)

train['date'] = train['date_x']
train.drop(['date_y','date_x'], 1, inplace=True)
