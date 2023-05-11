#!/usr/bin/python3
"""This program gets the title of all hot posts of a reddit subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=""):
    """Gets the titles recursively"""

    if (after == None):
        return hot_list

    if (len(hot_list) == 0):
        subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    else:
        subreddit_url = "https://reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

    response = requests.get(subreddit_url, headers=headers)

    if (response.status_code == 302 or response.status_code == 404):
        return None
    elif 'data' not in response.json():
        return None
    else:
        response_dict = response.json()
        for post in response_dict['data']['children']:
            hot_list.append(post['data']['title'])

    after = response_dict['data']['after']
    return recurse(subreddit, hot_list, after)
