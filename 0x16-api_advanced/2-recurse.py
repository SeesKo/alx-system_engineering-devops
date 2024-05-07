#!/usr/bin/python3
"""
Script that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests  # HTTP requests library


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches titles of all hot articles for a given subreddit.
    Returns list of titles. If subreddit is invalid/empty, returns None.
    """
    # Initialize hot_list if it is None
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    # Set a custom User-Agent
    headers = {'User-Agent': 'RedditRecurse/1.0 (Learning Project)'}

    # Get the response from the endpoint without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response status code isn't 200, return None
    if response.status_code != 200:
        return None

    # Parse the response JSON
    data = response.json()
    children = data.get("data", {}).get("children", [])

    # If there are no children, return None
    if not children:
        return None

    # Append the titles to the hot_list
    for post in children:
        title = post.get("data", {}).get("title", "No title")
        hot_list.append(title)

    # Check for the 'after' key to see if there's more data to fetch
    after = data.get("data", {}).get("after", None)

    # If there's an 'after', recurse with updated hot_list and 'after' value
    if after:
        return recurse(subreddit, hot_list, after)

    # If there's no more data to fetch, return the hot_list
    return hot_list
