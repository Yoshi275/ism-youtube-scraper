from channel_info import *
import numpy as np
import pandas as pd
from decouple import config

### COMMANDS TO RUN THIS:
### pip install -r requirements.txt
### python main.py

def main():
    print("In the format of a case-sensitive comma-separated list \ne.g.: j1mmyb0bba \ne.g.: j1mmyb0bba,PointlessBlog,MarcusButlerTv")
    youtuber_username_inputs = input("Enter YouTubers to retrieve videos from: \n")
    usernames_arr = youtuber_username_inputs.split(',')
    print(usernames_arr)
    for username in usernames_arr:
        # generate_csv_of_videos_from_youtuber(username)
        generate_csv_of_videos_from_youtube_channel_id(username)

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
    CSV_FILE_NAME = CHANNEL_NAME + "_videos.csv"
    generate_csv_of_videos(DEVELOPER_KEY, channel_id, CHANNEL_NAME, CSV_FILE_NAME)


def generate_csv_of_videos_from_youtuber(channel_name):
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    CHANNEL_NAME = channel_name
    CSV_FILE_NAME = CHANNEL_NAME + "_videos.csv"
    print("Retrieving {}'s videos".format(CHANNEL_NAME))

    channel_id = youtube_username_to_id(DEVELOPER_KEY, CHANNEL_NAME)
    if not channel_id:
        return
    else:
        generate_csv_of_videos(DEVELOPER_KEY, channel_id, CHANNEL_NAME, CSV_FILE_NAME)

if __name__ == "__main__":
    main()