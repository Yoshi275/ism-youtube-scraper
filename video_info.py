# -*- coding: utf-8 -*-

# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import requests
import html
import math
import dateutil

### definitions:
#### usernames: youtube.com/user/<USERNAME> in link
#### channel_id: youtube.com/channel/<channel_id> in link
#### video_id: youtube.com/watch?v=<video_id> in link
#### playlist_id: youtube.com/playlist?list=<playlist_id> in link

### instructions:
#### obtain the developer key from Google console, with access to the YouTube Data API V3 - instructions here: https://developers.google.com/youtube/v3/getting-started

def video_ids_to_viewcount(developer_key, video_ids, batch_size):
    # obtains a batch of video_ids stored in an array, with a batch_size indicated
    # queries all IDs in that array to return viewcount for each video, returned in array
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "videos"
    QUERY_PART = 'statistics'
    PAGE_QUERY_MAX_RESULTS = 50
    
    video_ids_str = ','.join(video_ids)
    query = {
        'part': QUERY_PART,
        'key': developer_key,
        'id': video_ids_str,
        'maxResults': PAGE_QUERY_MAX_RESULTS
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    response = requests.get(url, params=query)
    json_response = json.loads(response.text) 
    viewcounts_arr = {}
    for video in json_response['items']:
        video_id = video['id']
        viewcount = video['statistics']['viewCount']
        viewcounts_arr[video_id] = viewcount 
    return viewcounts_arr