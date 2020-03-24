import wtiproj01_lib as red
import json
import time
import sys

queue = "queue"
was_data = 1
frequency_per_second = sys.argv[1]
should_I_stop_after_10_s = sys.argv[2]
times_i_run = float(frequency_per_second) * 10
time_to_sleep = 1.0/float(frequency_per_second)
time_i_waited = 0
all_time_i_waited = 0

try:
    while 2 > 0 or not (should_I_stop_after_10_s == 1 and times_i_run <= 0) :
        try:
            json_data = red.get(queue)
            json_object = json.loads(json_data)
            json_formatted_str = json.dumps(json_object, indent=2)
            print(json_formatted_str)
            if was_data == 0:
                print("I waited for data for " + str(time_i_waited) + "s")
                all_time_i_waited += time_i_waited
                time_i_waited = 0
            was_data = 1
        except IndexError:
            time_i_waited = time_i_waited + time_to_sleep
            if was_data == 1:
                print("There's no more data")
            was_data = 0
        time.sleep(time_to_sleep)
        times_i_run = times_i_run - 1
except KeyboardInterrupt:
    if all_time_i_waited == 0: all_time_i_waited = time_i_waited
    print("I spent " + str(all_time_i_waited) + "s on waiting")

