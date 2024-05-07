#!/usr/bin/python3
"""
Script that queries the Reddit API and prints
a sorted count of given keywords.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, word_counter=None, after=None):
    """
    Recursively fetches titles of all hot articles for a given subreddit
    and counts the occurrences of given keywords.
    Prints a sorted count of the given keywords (case-insensitive).
    """
    # Initialize word_counter if not provided (for the first call)
    if word_counter is None:
        word_counter = Counter()

    # Construct the URL for fetching hot posts with optional
    # 'after' parameter for pagination
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    # Set a custom User-Agent
    headers = {'User-Agent': 'RedditKeywordCounter/1.0 (Learning Project)'}

    # Get the response from the endpoint without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If response status code isn't 200, return without printing anything
    if response.status_code != 200:
        return

    # Parse the response JSON
    data = response.json().get("data", {})
    children = data.get("children", [])

    # If there are no children, return without printing anything
    if not children:
        return

    # Loop through the titles of the hot posts
    for child in children:
        title = child.get("data", {}).get("title", "").lower()

        # Split the title into words
        words_in_title = title.split()

        # Count each keyword in the title
        for keyword in word_list:
            count = words_in_title.count(keyword.lower())
            if count > 0:
                word_counter[keyword.lower()] += count

    # Get the 'after' parameter for pagination
    after = data.get("after", None)

    # Recursively call the function if there's more data to fetch
    if after:
        count_words(subreddit, word_list, word_counter, after)

    # If no more data to fetch, print results in sorted order
    else:
        # Sort by count in descending order, then by word in ascending order
        sorted_word_counts = sorted(
            word_counter.items(),
            key=lambda item: (-item[1], item[0])
        )

        # Print the sorted word counts
        for word, count in sorted_word_counts:
            if count > 0:  # Skip words with no occurrences
                print(f"{word}: {count}")
