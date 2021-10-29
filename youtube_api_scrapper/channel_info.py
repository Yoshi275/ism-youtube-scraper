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

def youtube_username_to_id(developer_key, channel_name):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developer_key,
        'forUsername': channel_name,
        'part': 'id'
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    try:
        response = requests.get(url, params=query)
        json_response = json.loads(response.text)
        assert 'items' in json_response
    except AssertionError:
        print("YouTube username given is invalid. Please retry.")
        return
    else:
        channel_id = json_response['items'][0]['id']
        return channel_id

def youtube_id_to_search_statistics(developer_key, channel_id):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "search"
    QUERY_PART = 'snippet'
    PAGE_QUERY_MAX_RESULTS = 50
    query = {
        'part': QUERY_PART,
        'key': developer_key,
        'channelId': channel_id,
        'order': 'date',
        'type': 'video',
        'maxResults': PAGE_QUERY_MAX_RESULTS
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    response = requests.get(url, params=query)
    json_response = json.loads(response.text) 
    number_of_results = json_response['pageInfo']['totalResults']
    return number_of_results

def youtube_id_to_statistics(developer_key, channel_id):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developer_key,
        'id': channel_id,
        'part': 'statistics'
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    try:
        response = requests.get(url, params=query)
        json_response = json.loads(response.text)
        assert 'items' in json_response
    except AssertionError:
        print("YouTube ID given is invalid. Please retry.")
        return
    else:
        view_count = json_response['items'][0]['statistics']['viewCount']
        is_subscriber_count_hidden = json_response['items'][0]['statistics']['hiddenSubscriberCount']
        if is_subscriber_count_hidden:
            subscriber_count = 'hidden'
        else:
            subscriber_count = json_response['items'][0]['statistics']['subscriberCount']
        video_count = json_response['items'][0]['statistics']['videoCount']
        return view_count, subscriber_count, video_count

def youtube_id_to_channel_name(developer_key, channelId):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developer_key,
        'id': channelId,
        'part': 'snippet'
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    try:
        response = requests.get(url, params=query)
        json_response = json.loads(response.text)
        assert 'items' in json_response
    except AssertionError:
        print("YouTube ID given is invalid. Please retry.")
        return
    else:
        channel_name = json_response['items'][0]['snippet']['title']
        return channel_name

def get_all_videos_from(developer_key, channel_id):
    PAGE_QUERY_MAX_RESULTS = 50
    video_arr, last_published_video = get_max_query_videos_from(developer_key, channel_id, PAGE_QUERY_MAX_RESULTS, None)
    while do_earlier_videos_exist(developer_key, channel_id, last_published_video, PAGE_QUERY_MAX_RESULTS):
        print("New videos do exist")
        new_video_arr, last_published_video = get_max_query_videos_from(developer_key, channel_id, PAGE_QUERY_MAX_RESULTS, last_published_video)
        video_arr += new_video_arr
    return video_arr

def do_earlier_videos_exist(developer_key, channel_id, last_published_video, page_query_max_results):
    is_there_next_page, videos_arr = get_page_of_videos_from(developer_key, channel_id, None, page_query_max_results, last_published_video)
    if len(videos_arr) <= 1:        # seems like publishedBefore includes a video published at that exact time
        return False
    return True

def get_max_query_videos_from(developer_key, channel_id, page_query_max_results, published_before):
    TOTAL_QUERY_MAX_RESULTS = 500
    video_arr = []
    next_page_token, new_video_dict_page = get_page_of_videos_from(developer_key, channel_id, None, page_query_max_results, published_before)
    video_arr += new_video_dict_page

    while next_page_token != None:
        print("Adding {} more videos with page ID: {}".format(page_query_max_results, next_page_token))
        next_page_token, new_video_dict_page = get_page_of_videos_from(developer_key, channel_id, next_page_token, page_query_max_results, published_before)
        video_arr += new_video_dict_page
    last_video_published_date = video_arr[len(video_arr) - 1]['publish_time']
    print("Total number of videos found: {}; Last published video: {}".format(len(video_arr), dateutil.parser.parse(last_video_published_date)))
    return video_arr, last_video_published_date

def get_page_of_videos_from(developer_key, channel_id, next_page_token, page_query_max_results, published_before):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "search"
    QUERY_PART = 'snippet'
    video_arr = []

    query = {
        'part': QUERY_PART,
        'key': developer_key,
        'channelId': channel_id,
        'order': 'date',
        'type': 'video',
        'maxResults': page_query_max_results
    }
    if (next_page_token != None):
        query['pageToken'] = next_page_token
    if (published_before != None):
        query['publishedBefore'] = published_before

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    response = requests.get(url, params=query)
    json_response = json.loads(response.text) 
    if 'nextPageToken' in json_response:
        is_next_page_present = json_response['nextPageToken']
        print("Found next page token")
        print(is_next_page_present)
    else:
        is_next_page_present = False
        print("Next page not found")
    for search_result in json_response['items']:
        video_arr.append({
            'video_id': search_result['id']['videoId'],
            'channel_id': search_result['snippet']['channelId'],
            'title': html.unescape(search_result['snippet']['title']),
            'publish_time': search_result['snippet']['publishTime']
        })

    if (is_next_page_present):
        return is_next_page_present, video_arr
    else:
        return None, video_arr
    
def channel_id_to_uploads_playlist(developer_key, channel_id):
    # obtains the Youtuber's entire uploads playlist based on input channel_id given, pulling from YouTube Data API
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developer_key,
        'id': channel_id,
        'part': 'contentDetails'
    }

    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT

    try:
        response = requests.get(url, params=query)
        json_response = json.loads(response.text)
        assert 'items' in json_response
    except AssertionError:
        print("YouTube ID given is invalid. Please retry.")
        return
    else:
        channel_name = json_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return channel_name
    return