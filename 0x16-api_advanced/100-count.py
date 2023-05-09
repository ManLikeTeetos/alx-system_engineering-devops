#!/usr/bin/python3
""" Recursive function that queries the Reddit API
    parses the title of all hot articles, and prints a sorted count"""
import requests
import sys


import requests

def count_words(subreddit, word_list, word_count={}):
    if not word_list:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Softboi/0.0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()["data"]
    children = data["children"]
    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            if title.count(word) > 0:
                if word in word_count:
                    word_count[word] += title.count(word)
                else:
                    word_count[word] = title.count(word)

    if data["after"]:
        count_words(subreddit, word_list, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
