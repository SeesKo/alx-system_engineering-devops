#!/usr/bin/python3
"""
Script to query the Reddit API and return the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "CustomUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return (0)
    response = response.json()
    if "data" in response:
        return (response.get("data").get("subscribers"))
    else:
        return (0)
