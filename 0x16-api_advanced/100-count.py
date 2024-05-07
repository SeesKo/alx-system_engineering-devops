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
    if word_counter is None:
        word_counter = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'RedditKeywordCounter/1.0 (Learning Project)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        return

    for child in children:
        title = child.get("data", {}).get("title", "").lower()

        words_in_title = title.split()

        for keyword in word_list:
            count = words_in_title.count(keyword.lower())
            if count > 0:
                word_counter[keyword.lower()] += count

    after = data.get("after", None)

    if after:
        count_words(subreddit, word_list, word_counter, after)
    else:
        sorted_word_counts = sorted(
            word_counter.items(),
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_word_counts:
            if count > 0:
                print(f"{word}: {count}")
