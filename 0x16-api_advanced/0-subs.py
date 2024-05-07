#!/usr/bin/python3
"""
Script to query the Reddit API and return the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'SimpleRedditScript/1.0 (Python/3.10)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        elif response.status_code == 302:
            return 0
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except Exception as e:
        return 0
