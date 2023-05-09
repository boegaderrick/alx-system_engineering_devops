#!/usr/bin/python3
"""
    This module contains a function that makes an API call
"""
from requests import get
from json import loads


def number_of_subscribers(subreddit=None):
    """
        This function sends a request to the reddit api requesting
        information about a subreddit then returns the said subreddit's
        total number of subscribers to the caller.

        @subreddit: Name of subreddit to request
        @Return: Total number of subscribers on success
               : 0 on failure
    """
    if subreddit is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = loads(get(url).text)
    return (response.get('data').get('subscribers'))
