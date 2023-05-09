#!/usr/bin/python3
"""
    This module contains a function that makes an API call
"""
from requests import get


def recurse(subreddit, hot_list=[], page=None):
    """
        This function sends a request to the reddit api requesting
        information about a subreddit then appends the titles of all
        hot posts of the said subreddit to a list object.

        @subreddit: Name of subreddit to request
        @hot_list: List to contain the titles.
        @page:
            Link to the next page of the API response, in the first call
            it's value will be 'None' but with every response received
            the value of 'after' in 'data' in the response will be
            assigned to it. This will be used as the base case to aid
            in calling the funcion recursively. As long as the 'after'
            key doesn't equal 'null' the function will be called
            recursively to retrieve posts and the titles of all posts
            from all pages.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if page:
        url = url + '?after={}'.format(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/114.0.0.0 Safari/537.36 Edg/114.0.0.0'
    }
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code > 299:
        return None

    response = response.json()
    posts = response.get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))

    page = response.get('data').get('after')
    if page:
        recurse(subreddit, hot_list, page)

    return hot_list
