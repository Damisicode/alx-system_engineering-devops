#!/usr/bin/python3
"""This program gets the number of subscriber of a reddit subreddit"""
import requests

def number_of_subscribers(subreddit):
    subreddit_url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

    response = requests.get(subreddit_url, headers=headers)

    if (response.status_code == 302 or response.status_code == 404):
        return 0
    response_dict = response.json()

    if ('error' in response_dict):
        return 0
    elif ('subscribers' in response_dict['data']):
        return response_dict['data']['subscribers']
    else:
        return 0
