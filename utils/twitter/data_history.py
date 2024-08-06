import json
import pytz
import dateutil.parser
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

CET = pytz.timezone("Europe/Budapest")
BST = pytz.timezone("Europe/London")

tweets = []
with open("./tweets.json", "r") as twitterfile:
    tweets = json.load(twitterfile)


def get_tweet(id):
    for x in tweets:
        tw = x.get("tweet")
        tid = tw.get("id_str")
        if tid == str(id):
            return x
    logger.error("Tweet with ID: %d not found", id)
    return None


def get_text(tweet):
    return tweet.get("tweet").get("full_text")


def get_created_date(tweet):
    """Use BST so 1 AM marks a new day"""
    # '%Y-%m-%dT%H:%M:%S.%fZ'
    date_str = tweet.get("tweet").get("created_at")
    date_datetime = dateutil.parser.parse(date_str)
    result = date_datetime.astimezone(tz=BST).isoformat()

    return result


def download_image_attachment(daynum, t):
    tweet = t.get("tweet")
    includes = tweet.get("extended_entities")
    if includes is None:
        return None
    media = includes.get("media")
    if (media is None) or len(media) == 0:
        return None
    logger.info("Found %d media for %s", len(media), tweet.get("id"))
    result = []
    i = 0
    for item in media:
        if item.get("type") == "photo":
            url = item.get("media_url")
            alt_text = item.get("alt_text")
            filepath = f"assets/day-{daynum}_{i}.jpg"
            result.append(
                {
                    "url": url,
                    "alt_text": alt_text,
                    "filepath": filepath,
                    "type": "photo",
                }
            )
            logger.info("Image Attachment found %s", result)
            response = requests.get(url, timeout=600)
            with open(f"../../{filepath}", "wb") as attachment:
                attachment.write(response.content)
            logger.info("Attachment saved to %s", filepath)
            i += 1
        elif item.get("type") == "video":
            video_info = item.get("video_info")
            if video_info is None:
                logger.error("No video info...")
                break
            variants = video_info.get("variants")
            if variants is None:
                logger.error("No video info...")
                break

            for variant in variants:
                if (
                    variant.get("content_type") == "video/mp4"
                    and variant.get("bitrate") == "2176000"
                ):
                    url = variant.get("url")
                    alt_text = ""
                    filepath = f"assets/day-{daynum}.mp4"
                    result.append(
                        {
                            "url": url,
                            "alt_text": alt_text,
                            "filepath": filepath,
                            "type": "video",
                        }
                    )
                    logger.info("Video Attachment found %s", result)
                    response = requests.get(url, timeout=600)
                    with open(f"../../{filepath}", "wb") as attachment:
                        attachment.write(response.content)
                    logger.info("Attachment saved to %s", filepath)
                    i += 1
    return result


def get_public_metrics(tweet):
    retweet_count = tweet.get("tweet").get("retweet_count")
    like_count = tweet.get("tweet").get("favorite_count")
    reply_count = 0
    quote_count = 0
    return {
        "retweet_count": retweet_count,
        "reply_count": reply_count,
        "like_count": like_count,
        "quote_count": quote_count,
    }


def get_web_attachment_url(tweet):
    data = tweet
    entities = data.get("entities")
    if entities is None:
        return None
    urls = entities.get("urls")
    if (urls is None) or (len(urls) == 0):
        return None
    result = None
    for item in urls:
        if item.get("media_key"):
            # ignore image attachment
            continue
        result = {
            "title": item.get("expanded_url"),
            "url": item.get("expanded_url"),
        }
        logger.info("Web Attachment found %s", result)
        break  # stop at first
    return result
