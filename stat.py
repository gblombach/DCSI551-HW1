"""
###############################
    George Blombach
    USC ID 2416-0961-99
    DSCI 551 - Spring 2023
    Homework #1
    January 2023

    File:   stat.py
    Syntax: python3 stat.py aqi.csv aqi.json
    Desc:   stat.py reads aqi.csv and outputs aqi.json
###############################
"""

import pandas as pd
import sys

arg_len = len(sys.argv)
if arg_len == 3:
    # aqi_data = pd.read_csv("aqi.csv")
    aqi_data_file = sys.argv[1]
    aqi_json_file = sys.argv[2]
    aqi_data = pd.read_csv(aqi_data_file)
    # set datetime
    aqi_data['Date'] = pd.to_datetime(aqi_data.Date, format='%Y-%m-%d')

    # extract year and month from Date
    aqi_data['Year'] = pd.to_numeric(aqi_data['Date'].dt.strftime('%Y'))
    aqi_data['Month'] = pd.to_numeric(aqi_data['Date'].dt.strftime('%m'))
    # to remove leading zero use -m for linux, #m for windows

    # rename column
    aqi_data = aqi_data.rename(columns={'AQI Value': 'Avg AQI'})

    # calculate mean and print to JSON
    aqi_data.groupby(['Country', 'Year', 'Month'])['Avg AQI'].mean().round(1).reset_index().to_json(aqi_json_file,
                                                                                                    orient='records',
                                                                                                    indent=2)
else:
    print("The syntax is ' python3 stat.py aqi.csv aqi.json'")
