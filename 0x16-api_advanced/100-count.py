#!/usr/bin/python3
"""
    This module contains a function that makes an API call
"""
from requests import get


def count_words(subreddit, word_list, page=None, dictionary={}):
    """
        This function sends a request to the reddit api requesting
        information about a subreddit then searches for matching
        patterns of some words in the titles. All occurence of each
        word is recorded, after matching is finalised each word is printed
        alongside a combined total of its number of occurences in all
        titles.

        @subreddit: Name of subreddit to request
        @word_list: A list that contains words to match.
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
    if len(word_list) < 1:
        return

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
        return

    response = response.json()
    posts = response.get('data').get('children')
    for post in posts:
        title = post.get('data').get('title')
        for word in word_list:
            word = ' ' + word.lower() + ' '
            count = title.lower().count(word)
            if count > 0:
                word = word.strip()
                if dictionary.get(word):
                    dictionary[word] += count
                else:
                    dictionary[word] = count

    page = response.get('data').get('after')
    if page:
        count_words(subreddit, word_list, page, dictionary)
    else:
        foo = sorted(dictionary.values())
        order = 1 if foo[0] != foo[-1] else 0
        reverse = True if order == 1 else False
        final = sorted(dictionary.items(), key=lambda items: items[order],
                       reverse=reverse)
        if reverse is True:
            for i in range(len(final)):
                if i < len(final) - 1 and final[i][1] == final[i + 1][1]:
                    if final[i][0] > final[i + 1][0]:
                        temp = final[i]
                        final[i] = final[i + 1]
                        final[i + 1] = temp

        for key, value in final:
            print(key + ': ' + str(value))
