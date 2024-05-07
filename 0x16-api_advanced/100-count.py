#!/usr/bin/python3
"""
Script that queries the Reddit API and prints
a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively fetches titles of all hot articles for a given subreddit
    and counts the occurrences of given keywords.
    """
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                counts[word_lower] = counts.get(
                        word_lower, 0) + title.count(word_lower)

    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
