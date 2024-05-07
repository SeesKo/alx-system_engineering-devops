#!/usr/bin/python3
"""
Script to query the Reddit API and return the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for success status code
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        else:
            return 0
    except requests.RequestException:
        # If there's any error with the request, return 0
        return 0
