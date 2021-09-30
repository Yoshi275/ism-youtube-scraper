from channel_info import *
from playlist_info import *
import numpy as np
import pandas as pd
from decouple import config

### COMMANDS TO RUN THIS:
### pip install -r requirements.txt
### python id_to_uploads_playlist.py

def id_to_uploads_playlist():
    print("In the format of a case-sensitive comma-separated list \ne.g.: UCst9GLZ-X47MxWBmx9cCrKA \ne.g.: UCst9GLZ-X47MxWBmx9cCrKA, UCJ47W_WzuzbHaONWB5a9i7w, UCk5azh7kjYWMkWQsLrqn_9w")
    print("Accepts ONLY channel IDs (/channel/<CHANNEL_ID>)\n")
    channel_id_inputs = input("Enter YouTubers to retrieve videos from: \n")
    input_arr = channel_id_inputs.split(',')
    channel_id_arr = [i.strip() for i in input_arr]
    print(channel_id_arr)
    for channel_id in channel_id_arr:
        generate_csv_of_videos_from_youtube_channel_id(channel_id)

def generate_csv_of_videos_from_youtube_channel_id(channel_id):
    try:
        DEVELOPER_KEY = config('DEVELOPER_KEY', default='')
    except:
        print("API key loading failed. Please check that you have a .env file containing the DEVELOPER_KEY variable, a valid YouTube Data API key")
        return
    channel_name = youtube_id_to_channel_name(DEVELOPER_KEY, channel_id)
    uploads_playlist = channel_id_to_uploads_playlist(DEVELOPER_KEY, channel_id)
    if not uploads_playlist:
        print("ID does not have a Uploads playlist. Please try again.")
        return
    CHANNEL_NAME = channel_name
    CSV_FILE_NAME = "output/" + CHANNEL_NAME + "_uploads_playlist_videos.csv"
    print("Retrieving videos for {}".format(channel_name))

    videos = get_all_videos_from_playlist_id(DEVELOPER_KEY, uploads_playlist)
    if not videos:
        print("Video retrieval failed. Please try again.")
        return
    temp_videos_df = pd.DataFrame(videos)
    print(temp_videos_df)
    videos_df = pd.DataFrame(columns=['VideoID', 'Title', 'UploaderUsername', 'DateUploaded', 'VideoLink', 'Status', 'Description', 'ThumbnailLink', 'IsCollab', 'Featuring', 'RelatedVideos', 'CollaboratorId'])
    print("generating csv at {}".format(CSV_FILE_NAME))

    for index, row in temp_videos_df.iterrows():
        # is_video_collab = is_collaboration()
        new_row = {
            'VideoID': row['video_id'],
            'Title': row['title'],
            'UploaderId': row['channel_id'],
            'DateUploaded': row['published_time'],
            'VideoLink': "youtube.com/watch?v=" + row['video_id'],
            'Status': row['privacy_status'],
            'Description': row['description'],
            'ThumbnailLink': row['thumbnail_link']
        }
        videos_df = videos_df.append(new_row, ignore_index=True)
    videos_df.to_csv(CSV_FILE_NAME, index=False)

if __name__ == "__main__":
    id_to_uploads_playlist()