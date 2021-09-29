from channel_info import *
import numpy as np
import pandas as pd
from decouple import config

# input: csv table with second column "YoutubeUsername" that contains a Youtuber's Username (/user/<username>)
# output: csv table with first column "ChannelID" filled, based on Youtuber's username
def fill_all_channel_ids(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)

    for index, row in df.iterrows():
        if (not pd.isna(df.loc[index, 'YoutubeUsername'])) and (pd.isna(df.loc[index, 'ChannelID'])):
            print(df.loc[index, 'YoutubeUsername'])
            youtube_username = df.at[index, 'YoutubeUsername']
            channel_id = youtube_username_to_id(developer_key, youtube_username)
            df.at[index, 'ChannelID'] = channel_id
    df.to_csv(csv_output_file, index=False)
    return

# input: csv table with first col "ChannelID" filled, and second col "YoutuberUsername" optionally filled
# output: csv table with third col "GoogleName" filled, if "GoogleName" != "YoutuberUsername"
def fill_all_google_names(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)
    df['GoogleName'] = df['GoogleName'].astype(object)

    for index, row in df.iterrows():
        print(df.loc[index, 'ChannelID'])
        channel_id = df.at[index, 'ChannelID']
        channel_name = youtube_id_to_channel_name(developer_key, channel_id)
        if pd.isna(df.loc[index, 'YoutubeUsername']) or (channel_name != df.loc[index, 'YoutubeUsername']):
        # if channel name is different from Youtube username, then add channel name as GoogleName
            print(channel_name)
            df.at[index, 'GoogleName'] = channel_name
    df.to_csv(csv_output_file, index=False)
    return

# input: csv table with first col "ChannelID" filled
# output: csv table with third, fourth, sixth col "ViewCount", "SubscriberCount" and "VideosAvailable" filled respectively
def fill_all_statistics(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)
    df['ViewCount'] = df['ViewCount'].astype(object)
    df['SubscriberCount'] = df['SubscriberCount'].astype(object)
    df['VideosAvailable'] = df['VideosAvailable'].astype(object)

    for index, row in df.iterrows():
        print(df.loc[index, 'ChannelID'])
        channel_id = df.at[index, 'ChannelID']
        view_count, subscriber_count, video_count = youtube_id_to_statistics(developer_key, channel_id)
        print(view_count, subscriber_count, video_count)
        df.at[index, 'ViewCount'] = view_count
        df.at[index, 'SubscriberCount'] = subscriber_count
        df.at[index, 'VideosAvailable'] = video_count
    df.to_csv(csv_output_file, index=False)
    return

def fill_result_statistics(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)
    df['ViewCount'] = df['VideosFound'].astype(object)

    for index, row in df.iterrows():
        if index >= 99:
            print(df.loc[index, 'ChannelID'])
            channel_id = df.at[index, 'ChannelID']
            number_of_findable_videos = youtube_id_to_search_statistics(developer_key, channel_id)
            df.at[index, 'VideosFound'] = number_of_findable_videos
    df.to_csv(csv_output_file, index=False)
    return

# removes all whitespaces from YoutubeUsername column
def remove_all_whitespaces(developer_key, csv_input_file, csv_output_file):
    df = pd.read_csv(csv_input_file)
    print(df)
    for index, row in df.iterrows():
        if not pd.isna(df.loc[index, 'YoutubeUsername']):
            df.at[index, 'YoutubeUsername'] = row['YoutubeUsername'].strip()
        if not pd.isna(df.loc[index, 'ChannelID']):
            df.at[index, 'ChannelID'] = row['ChannelID'].strip()
        print(df.at[index, 'YoutubeUsername'])
    df.to_csv(csv_output_file, index=False)

def main():
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    CSV_INPUT_FILE = "channel_info_raw_data.csv"
    CSV_OUTPUT_FILE = CSV_INPUT_FILE
    # remove_all_whitespaces(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)
    # fill_all_channel_ids(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)
    # fill_all_google_names(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)
    # fill_all_statistics(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)
    fill_result_statistics(DEVELOPER_KEY, CSV_INPUT_FILE, CSV_OUTPUT_FILE)

if __name__ == "__main__":
    main()