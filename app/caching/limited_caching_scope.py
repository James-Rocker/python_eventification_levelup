#!/usr/bin/env python
import requests

cache = dict()


def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text


def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]


# see how we only printed the fetching article once. This is because we are caching the article
get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")

# this is useful if we have a set limit of objects we are searching for
# but when looking at larger quantities, the dict can only contain so much
