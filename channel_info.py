# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import requests
import html
import math

# scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def youtube_username_to_id(developerKey, channelName):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developerKey,
        'forUsername': channelName,
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

def youtube_id_to_statistics(developerKey, channel_id):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developerKey,
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

def youtube_id_to_channel_name(developerKey, channelId):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "channels"

    query = {
        'key': developerKey,
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
    TOTAL_QUERY_MAX_RESULTS = 500
    PAGE_QUERY_MAX_RESULTS = 50
    TOTAL_PAGES_LIMIT = math.floor(TOTAL_QUERY_MAX_RESULTS / PAGE_QUERY_MAX_RESULTS)
    video_arr = []
    next_page_token, new_video_dict_page = get_page_of_videos_from(developer_key, channel_id, None, PAGE_QUERY_MAX_RESULTS)
    video_arr += new_video_dict_page

    while next_page_token != None:
        print("Adding 50 more videos with page ID: {}".format(next_page_token))
        next_page_token, new_video_dict_page = get_page_of_videos_from(developer_key, channel_id, next_page_token, PAGE_QUERY_MAX_RESULTS)
        video_arr += new_video_dict_page
    print("Total number of videos found: {}\n".format(len(video_arr)))
    return video_arr

def get_page_of_videos_from(developer_key, channel_id, next_page_token, page_query_max_results):
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "search"
    QUERY_PART = 'snippet'
    video_arr = []

    if (next_page_token != None):
        query = {
            'part': QUERY_PART,
            'key': developer_key,
            'channelId': channel_id,
            'order': 'date',
            'type': 'video',
            'maxResults': page_query_max_results,
            'pageToken': next_page_token
        }
    else:
        query = {
            'part': QUERY_PART,
            'key': developer_key,
            'channelId': channel_id,
            'order': 'date',
            'type': 'video',
            'maxResults': page_query_max_results
        }

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

    # if (len(video_arr) < )

    if (is_next_page_present):
        return is_next_page_present, video_arr
    else:
        return None, video_arr
    
