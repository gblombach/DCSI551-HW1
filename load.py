"""
###############################
    George Blombach
    USC ID 2416-0961-99
    DSCI 551 - Spring 2023
    Homework #1
    January 2023

    file:   load.py
    Syntax: python3 load.py aqi.json <database-url>/aqi.json
    Command:python3 load.py aqi.json https://blombach-dsci551-default-rtdb.firebaseio.com/aqi.json
    Desc:   load.py loads aqi.json into Firebase database

    https://blombach-dsci551-default-rtdb.firebaseio.com/

###############################
"""
import sys
import json as js
import requests

arg_len = len(sys.argv)
if arg_len == 3:
    # aqi_data = pd.read_csv("aqi.csv")
    aqi_json_file = sys.argv[1]
    firebase_db = sys.argv[2]

    #load json data from file
    json_file = open(aqi_json_file)
    json_data = js.load(json_file)
    print(json_data)

    #requests.delete(url=firebase_db)
    #write json data to firebase
    requests.put(url=firebase_db, json=json_data)

else:
    print("The syntax is ' python3 load.py aqi.json <database-url>/aqi.json'")
