from channel_info import *
import numpy as np
import pandas as pd
from decouple import config

### COMMANDS TO RUN THIS:
### pip install -r requirements.txt
### python channels_to_ids.py

def channel_usernames_to_ids():
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return

    print("In the format of a case-sensitive comma-separated list \ne.g.: j1mmyb0bba,PointlessBlog")
    print("Accepts ONLY usernames (/user/<USERNAME>)\n")
    username_inputs = input("Enter YouTubers to retrieve videos from: \n")
    input_arr = username_inputs.split(',')
    username_arr = [i.strip() for i in input_arr]
    print(username_arr)
    channel_ids = []
    for username in username_arr:
        new_channel_id = youtube_username_to_id(DEVELOPER_KEY, username)
        if new_channel_id != None:
            channel_ids.append(new_channel_id)
    print(",".join(channel_ids))

if __name__ == "__main__":
    channel_usernames_to_ids()