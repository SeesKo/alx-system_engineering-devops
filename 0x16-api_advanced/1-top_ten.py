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
        response.raise_for_status()

        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children'][:10]
            for post in posts:
                print(post['data'].get('title', 'No Title'))
        else:
            print("No posts found")
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    except ValueError as e:
        print("Error parsing JSON response")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
