#!/usr/bin/python3
"""This program gets the title of top ten of hot posts of a reddit subreddit"""
import requests

def top_ten(subreddit):
    subreddit_url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

    response = requests.get(subreddit_url, headers=headers)

    if (response.status_code == 302 or response.status_code == 404):
        return 0
    response_dict = response.json()

    if ('error' in response_dict):
        return 0
    elif (response_dict['data']['dist'] == 10):
        for i in range(10):
            print(response_dict['data']['children'][i]['data']['title'])
        return 0
    else:
        return 0
