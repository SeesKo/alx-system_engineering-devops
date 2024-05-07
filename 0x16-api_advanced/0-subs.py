#!/usr/bin/python3
"""
Script to query the Reddit API and return the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid or unavailable,
    it returns 0.
    """
    # Construct the URL for the "about" endpoint for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent
    headers = {
        "User-Agent": "SubredditInfoFetcher/1.0 (Learning Project)"
    }

    # Send the HTTP request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is not 200 or if it's empty
    if response.status_code != 200 or not response.text.strip():
        return 0

    # Try to parse the response as JSON
    try:
        data = response.json()  # Attempt to parse JSON
        if "data" not in data:
            return 0
        subscribers = data["data"].get("subscribers", 0)
        return subscribers
    except ValueError:
        # If the JSON parsing fails, return 0
        return 0
