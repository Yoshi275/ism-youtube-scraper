### definitions:
#### video_id: youtube.com/watch?v=<video_id> in link
#### playlist_id: youtube.com/playlist?list=<playlist_id> in link

import requests
import html
import json

def get_all_videos_from_playlist_id(developer_key, playlist_id):
    # returns all videos in a playlist
    ## for uploads playlists, ordered by newest -> oldest
    video_arr = []
    next_page_token, new_video_dict_page = get_page_of_videos_from_playlist_id(developer_key, playlist_id, None)

    while next_page_token != None:
        next_page_token, new_video_dict_page = get_page_of_videos_from_playlist_id(developer_key, playlist_id, next_page_token)
        video_arr += new_video_dict_page
    print("Total number of videos found: {}".format(len(video_arr)))
    # console.log(video_arr)
    return video_arr

def get_page_of_videos_from_playlist_id(developer_key, playlist_id, next_page_token):
    PAGE_QUERY_MAX_RESULTS = 50
    QUERY_PARTS = 'snippet, contentDetails, status'
    YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3"
    YOUTUBE_API_ENDPOINT = "playlistItems"

    video_arr = []
    url = YOUTUBE_API_URL + "/" + YOUTUBE_API_ENDPOINT
    query = {
        'part': QUERY_PARTS,
        'key': developer_key,
        'playlistId': playlist_id,
        'maxResults': PAGE_QUERY_MAX_RESULTS
    }

    if (next_page_token != None):
        query['pageToken'] = next_page_token
    
    response = requests.get(url, params=query)
    json_response = json.loads(response.text)
    if 'nextPageToken' in json_response:
        following_page_id = json_response['nextPageToken']
        print("Found next page token {}".format(following_page_id))
    else:
        following_page_id = None
        print("No next page found")
    for search_result in json_response['items']:
        video_arr.append({
            'video_id': search_result['contentDetails']['videoId'],
            'title': html.unescape(search_result['snippet']['title']),
            'channel_id': search_result['snippet']['channelId'],
            'description': html.unescape(search_result['snippet']['title']),
            'thumbnail_link': search_result['snippet']['thumbnails']['default']['url'],
            'published_time': search_result['contentDetails']['videoPublishedAt'],
            'privacy_status': search_result['status']['privacyStatus']
        })
    
    return following_page_id, video_arr