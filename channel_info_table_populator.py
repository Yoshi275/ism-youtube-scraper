from channel_info import *
import numpy as np
import pandas as pd
from decouple import config

# input: csv table with second column "YoutubeUsername" that contains a Youtuber's Username (/user/<username>)
# output: csv table with first column "ChannelID" filled, based on Youtuber's username
def fill_all_channel_ids(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)

    for index, row in df.iterrows():
        if not pd.isna(df.loc[index, 'YoutubeUsername']) and pd.isna(df.loc[index, 'ChannelID']):
            print(df.loc[index, 'YoutubeUsername'])
            youtube_username = df.at[index, 'YoutubeUsername']
            channel_id = youtube_username_to_id(developer_key, youtube_username)
            df.at[index, 'ChannelID'] = channel_id
    df.to_csv(csv_output_file, index=False)
    return

# input: csv table with first col "ChannelID" filled, and second col "YoutuberUsername" optionally filled
# output: csv table with third col "GoogleName" filled, if "GoogleName" != "YoutuberUsername"
def fill_all_google_names(developer_key, csv_input_file, csv_output_file):
    return

# removes all whitespaces from YoutubeUsername column
def remove_all_whitespaces(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)
    print(df)
    for index, row in df.iterrows():
        if not pd.isna(df.loc[index, 'YoutubeUsername']):
            df.at[index, 'YoutubeUsername'] = row['YoutubeUsername'].strip()
            print(df.at[index, 'YoutubeUsername'])
    df.to_csv(csv_output_file, index=False)

def main():
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    CSV_INPUT_FILE = "channel_info_raw_data.csv"
    CSV_OUTPUT_FILE = "test.csv"
    fill_all_channel_ids(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)

if __name__ == "__main__":
    main()