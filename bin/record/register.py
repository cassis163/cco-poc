import pandas as pd
import os
import datetime, time

log_path = os.getcwd() + '/records/log.csv'

if os.path.isfile(log_path):
    df = pd.read_csv(log_path, index_col=[0])
else:
    df = pd.DataFrame(columns=[
        'Time Elapsed',
        'Timestamp'
    ])

def register(time_elapsed):
    global df
    df = df.append(pd.Series(data={
        'Time Elapsed': time_elapsed,
        'Timestamp': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    }), ignore_index=True)

    df.to_csv(log_path)