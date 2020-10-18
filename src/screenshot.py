import requests
import base64
import os
import json
import logging

import selenium
from fetch_thread import get_api, get_tweet, update_urls
from screenshot_selenium import save_screenshot

logging.basicConfig(
    format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I_%M_%S %p',
    filename='log_file',
    level=logging.INFO
)

def delete_images(photo_list):
    for photo in photo_list:
        try:
            os.remove(photo)
        except OSError:
            pass

def save_images(url):
    api = get_api()
    tweet = get_tweet(url)
    urls = [url]
    urls.extend(update_urls(tweet, api))
    logging.info('screenshot/save_images: URLs fetched')
    for url in urls:
        logging.info('screenshot/save_images: ' + url)
    
    count = 0
    for url in urls:
        save_image(url, "desktop", tweet.user.screen_name + "_" + str(count))
        count += 1
    base_str = os.path.join(os.getcwd(), 'images')
    return [os.path.join(base_str, tweet.user.screen_name + "_" + str(_count) + ".png") for _count in range(count)]

def save_image(url, mode, name):
    save_screenshot(url, name)