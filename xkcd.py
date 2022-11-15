import requests
import random

def random_comic_site():
    r = requests.get('https://c.xkcd.com/random/comic/')
    site = r.text.split("""
""")
    return site

def random_comic():
    comic = []
    site = random_comic_site()
    image_link = site[84][48:].partition("\"")[0]
    comic.append(image_link)
    comic_title = site[64][17:][:-6]
    comic.append(comic_title)
    return comic

def comic_image_bytes():
    r = requests.get(comic_link())
    return r.content
