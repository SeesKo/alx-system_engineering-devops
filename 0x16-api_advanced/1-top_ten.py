#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'TopTenHotPosts/1.0 (Python/3.10)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts[:10]:
                print(post['data'].get('title', 'No Title'))
        elif response.status_code in {302, 404}:
            print("None")
        else:
            print("None")
    except Exception as e:
        print("None")
