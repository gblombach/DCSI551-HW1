"""
###############################
    George Blombach
    USC ID 2416-0961-99
    DSCI 551 - Spring 2023
    Homework #1
    January 2023

    File:   search.py
    Syntax: python3 search.py <database-url>/aqi.json 20 30
    Command:python3 search.py https://blombach-dsci551-default-rtdb.firebaseio.com/aqi.json 20 30

    Desc:   search.py will find all countries (with months and years) whose average AQI is between 20 and 30,
            inclusive. You can expect the second argument would always be smaller than or equal to the
            third argument. You can also expect the .indexOn has been set properly.

###############################
"""

import sys
import requests
import pandas as pd
import json

arg_len = len(sys.argv)
if arg_len == 4:
    # aqi_data = pd.read_csv("aqi.csv")
    firebase_db = sys.argv[1]
    range_low = sys.argv[2]
    range_high = sys.argv[3]
    query = '?orderBy="Avg AQI"&startAt=' + range_low + '&endAt=' + range_high
    results = requests.get(firebase_db + query)
    df = pd.read_json(results.text, orient='index')
    print(df[['Country', 'Month', 'Year']].to_string())
else:
    print("The syntax is ' python3 search.py <database-url>/aqi.json <low> <high>'")