#!/usr/bin/python3
"""
    This module contains a function that makes an API call
"""
from requests import get


def top_ten(subreddit):
    """
        This function sends a request to the reddit api requesting
        information about a subreddit then prints the first ten hot
        posts of the said subreddit.

        @subreddit: Name of subreddit to request
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0'
    }
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code > 299:
        print('None')
        return

    response = response.json()
    posts = response.get('data').get('children')
    for i in range(10):
        print(posts[i].get('data').get('title'))
