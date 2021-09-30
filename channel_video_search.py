from channel_info import *
import numpy as np
import pandas as pd
from decouple import config

### COMMANDS TO RUN THIS:
### pip install -r requirements.txt
### python channel_video_search.py

def channel_video_search():
    print("In the format of a case-sensitive comma-separated list \ne.g.: danisnotonfire \ne.g.: j1mmyb0bba,PointlessBlog,id=UCPvi4_6AZtfND4ILv82s3wA")
    print("Accepts channel IDs (/channel/<CHANNEL_ID>) or usernames (/user/<USERNAME>) \nPut 'id=' in front of ID to retrieve videos by ID instead.")
    youtuber_username_or_id_inputs = input("Enter YouTubers to retrieve videos from: \n")
    input_arr = youtuber_username_or_id_inputs.split(',')
    usernames_or_id_arr = [i.strip() for i in input_arr]
    print(usernames_or_id_arr)
    for username_or_id in usernames_or_id_arr:
        if username_or_id[0:3] == "id=":
            youtube_channel_id = username_or_id[3:]
            generate_csv_of_videos_from_youtube_channel_id(youtube_channel_id)
        else:
            generate_csv_of_videos_from_youtuber(username_or_id)


def generate_csv_of_videos(developer_key, channel_id, uploader_username_or_id, csv_file_name):
    videos = get_all_videos_from(developer_key, channel_id)
    if not videos:
        return
    tempVideosDf = pd.DataFrame(videos)    
    videosDf = pd.DataFrame(columns=['Id', 'Title', 'UploaderUsername', 'DateUploaded', 'VideoLink', 'Status', 'IsCollab']) 

    for index, row in tempVideosDf.iterrows():
        new_row = {
            'Id': row['video_id'],
            'Title': row['title'],
            'UploaderUsername': uploader_username_or_id,
            'DateUploaded': row['publish_time'],
            'VideoLink': "youtube.com/watch?v=" + row['video_id'],
            'Status': 'Public',
            'IsCollab': ''
        }
        videosDf = videosDf.append(new_row, ignore_index=True)
    videosDf.to_csv(csv_file_name, index=False)

def generate_csv_of_videos_from_youtube_channel_id(channel_id):
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    channel_name = youtube_id_to_channel_name(DEVELOPER_KEY, channel_id)
    if not channel_id:
        return
    print("Retrieving {}'s videos".format(channel_name))
    CHANNEL_NAME = channel_name
    CSV_FILE_NAME = "output/" + CHANNEL_NAME + "_videos.csv"
    generate_csv_of_videos(DEVELOPER_KEY, channel_id, CHANNEL_NAME, CSV_FILE_NAME)


def generate_csv_of_videos_from_youtuber(channel_name):
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    CHANNEL_NAME = channel_name
    CSV_FILE_NAME = "output/" + CHANNEL_NAME + "_videos.csv"
    print("Retrieving {}'s videos".format(CHANNEL_NAME))

    channel_id = youtube_username_to_id(DEVELOPER_KEY, CHANNEL_NAME)
    if not channel_id:
        return
    else:
        generate_csv_of_videos(DEVELOPER_KEY, channel_id, CHANNEL_NAME, CSV_FILE_NAME)

if __name__ == "__main__":
    channel_video_search()