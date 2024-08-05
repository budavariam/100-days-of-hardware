import requests
import dotenv
import logging
import re
import os
from dotenv import load_dotenv
import progress
import pytz
import dateutil.parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

CET=pytz.timezone('Europe/Budapest')
BST=pytz.timezone('Europe/London')
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def get_tweet(id):
    url=f"https://api.twitter.com/2/tweets/{id}?tweet.fields=attachments,created_at,entities,source,text,public_metrics&expansions=attachments.media_keys&media.fields=alt_text,media_key,type,url,variants&user.fields=created_at,id,name,url,username"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    tweet = requests.get(url, headers=headers).json()
    logger.info("Got data for id:%s data:%s", id, tweet)
    return tweet

def get_text(tweet):
    return tweet.get('data').get('text')

def get_created_date(tweet):
    """ Use BST so 1 AM marks a new day """
    # '%Y-%m-%dT%H:%M:%S.%fZ'
    date_str=tweet.get('data').get('created_at')
    date_datetime=dateutil.parser.isoparse(date_str)
    result = date_datetime.astimezone(tz=BST).isoformat()
    return result

def download_image_attachment(daynum, tweet):
    includes = tweet.get('includes')
    if includes is None:
        return None
    media = includes.get('media')
    if ((media is None) or len(media) == 0):
        return None
    result = None
    for item in media:
        if item.get('type') == "photo":
            url = item.get('url')
            alt_text = item.get('alt_text')
            filepath = f"assets/day-{daynum}.jpg"
            result = {
                'url': url,
                'alt_text': alt_text,
                'filepath': filepath,
            }
            logger.info("Image Attachment found", result)
            response = requests.get(url)
            with open(f"../../{filepath}", "wb") as attachment:
                attachment.write(response.content)
            logger.info("Attachment saved to %s", filepath)
            break # stop at first attachment
    return result

def get_public_metrics(tweet):
    # {'retweet_count': 0, 'reply_count': 0, 'like_count': 0, 'quote_count': 0}
    result=tweet.get('data').get('public_metrics')
    return result

def get_web_attachment_url(tweet):
    data=tweet.get('data')
    entities = data.get('entities')
    if entities is None:
        return None
    urls = entities.get('urls')
    if (urls is None) or (len(urls) == 0):
        return None
    result = None
    for item in urls:
        if item.get('media_key'):
            # ignore image attachment
            continue
        result = {
            'title': item.get('title'),
            'url': item.get('expanded_url'),
        }
        logger.info("Web Attachment found %s", result)
        break # stop at first
    return result