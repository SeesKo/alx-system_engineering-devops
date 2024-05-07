#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests  # HTTP requests library


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot
    posts listed for a given subreddit.
    If the subreddit is invalid or not reachable, prints 'None'.
    """
    # Construct the URL for the hot posts endpoint with a limit of 10
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditClient/0.1'}

    # Get the response from the endpoint, without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the status code isn't 200, consider it an invalid subreddit
    if response.status_code != 200:
        print("None")
        return

    # Parse the response data
    data = response.json()
    children = data.get("data", {}).get("children", [])

    # If no hot posts are found, consider it invalid
    if not children:
        print("None")
        return

    # Print the titles of the top 10 hot posts
    for post in children:
        title = post.get("data", {}).get("title", "No title")
        print(title)
