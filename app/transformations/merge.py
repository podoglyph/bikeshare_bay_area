import os
import pandas as pd
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime

from trip import trips_train
from weather import weather_train


trips_weather_train = trips_train.merge(weather_train, on = trips_train.date)

# setup dataframes
trips_weather_train["date"] = trips_weather_train["date_y"]
trips_weather_train.drop(["date_x", "date_y"], 1, inplace=True)

calendar = USFederalHolidayCalendar()
holidays = calendar.holidays(start=trips_weather_train.date.min(), end=trips_weather_train.date.max())

us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
business_days = pd.DatetimeIndex(start=trips_weather_train.date.min(), end=trips_weather_train.date.max(), freq=us_bd)

business_days = pd.to_datetime(business_days, format='%Y/%m/%d').date
holidays = pd.to_datetime(holidays, format='%Y/%m/%d').date

trips_weather_train['business_day'] = trips_weather_train.date.isin(business_days)
trips_weather_train['holiday'] = trips_weather_train.date.isin(holidays)

trips_weather_train.business_day = trips_weather_train.business_day.map(lambda x: 1 if x == True else 0)
trips_weather_train.holiday = trips_weather_train.holiday.map(lambda x: 1 if x == True else 0)

trips_weather_train['year'] = pd.to_datetime(trips_weather_train['date']).dt.year
trips_weather_train['month'] = pd.to_datetime(trips_weather_train['date']).dt.month
trips_weather_train['weekday'] = pd.to_datetime(trips_weather_train['date']).dt.weekday

# seems to be setup for training now.

print(trips_weather_train)
