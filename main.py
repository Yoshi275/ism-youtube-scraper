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
        generate_csv_of_videos_from_youtuber(username)

def generate_csv_of_videos_from_youtuber(channel_name):
    DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    CHANNEL_NAME = channel_name
    FILE_NAME = CHANNEL_NAME + "_videos.json" 
    CSV_FILE_NAME = CHANNEL_NAME + "_videos.csv"
    print("Retrieving {}'s videos".format(CHANNEL_NAME))

    channel_id = youtube_username_to_id(DEVELOPER_KEY, CHANNEL_NAME)
    if not channel_id:
        return
    videos = get_all_videos_from(DEVELOPER_KEY, channel_id)
    if not videos:
        return
    with open(FILE_NAME, "w") as write_file:
        json.dump(videos, write_file)
    df = pd.read_json(FILE_NAME)
    # video_id, channel_id, title, publish_time
    videosDf = pd.DataFrame(columns=['Id', 'Title', 'UploaderUsername', 'DateUploaded', 'VideoLink', 'Status', 'IsCollab']) 

    for index, row in df.iterrows():
        new_row = {
            'Id': row['video_id'],
            'Title': row['title'],
            'UploaderUsername': CHANNEL_NAME,
            'DateUploaded': row['publish_time'],
            'VideoLink': "youtube.com/watch?v=" + row['video_id'],
            'Status': 'Public',
            'IsCollab': ''
        }
        videosDf = videosDf.append(new_row, ignore_index=True)

    videosDf.to_csv(CSV_FILE_NAME, index=False)

if __name__ == "__main__":
    main()