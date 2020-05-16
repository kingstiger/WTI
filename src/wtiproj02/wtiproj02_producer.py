from witproj01 import wtiproj01_lib as red
import pandas as pd
import time
import sys

queue = "queue"
frequency_per_second = sys.argv[1]
time_to_sleep = 1.0 / float(frequency_per_second)

# columns: userID \t movieID \t rating \t date_day \t date_month \t date_year \t date_hour \t date_minute \t date_second

dataframe = pd.read_csv("/home/peter/Studia/WTI/user_ratedmovies.dat", sep='\t')
col_names = dataframe.columns
is_odd = 0

for row in dataframe.iterrows():
    for pair in row:
        if is_odd == 0:
            is_odd = 1
        elif is_odd == 1:
            red.push(pair.to_json(), queue)
            print(pair.to_json())
            is_odd = 0
            time.sleep(time_to_sleep)
