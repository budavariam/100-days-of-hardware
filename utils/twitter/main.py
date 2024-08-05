import requests
import dotenv
import logging
import re
import os
from dotenv import load_dotenv
import progress
import pytz
import dateutil.parser

if True:
    from data_history import (
        get_created_date,
        get_public_metrics,
        get_text,
        get_tweet,
        get_web_attachment_url,
        download_image_attachment,
    )
else:
    from data_api import (
        get_created_date,
        get_public_metrics,
        get_text,
        get_tweet,
        get_web_attachment_url,
        download_image_attachment,
    )

load_dotenv()  # take environment variables from .env.
ADD_THOUGHTS = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

IDS = progress.IDS


def get_last_visited_day():
    with open("./LAST_DAY", "r") as lastday:
        data = lastday.readline()
        return int(data)
    return None


def update_last_line(num):
    with open("./LAST_DAY", "w") as lastday:
        lastday.write(str(num))


def update_stats(stat_lines):
    header = "daynum,id,date,retweet_count,reply_count,like_count,quote_count" + "\n"
    # todo make it update the last N lines as well, not in a greedy way maybe be smart and handle it as csv, ffirst collect then update the data
    final = [header]
    with open("./STATS", "w") as stats:
        for data in stat_lines:
            [tweet_id, daynum, created_date, public_metrics] = data
            # public_metrics: {'retweet_count': 1, 'reply_count': 1, 'like_count': 1, 'quote_count': 0}
            stat_data = [
                str(daynum),
                str(tweet_id),
                created_date.split("T")[0],
                str(public_metrics.get("retweet_count")),
                str(public_metrics.get("reply_count")),
                str(public_metrics.get("like_count")),
                str(public_metrics.get("quote_count")),
            ]
            stat_line = ",".join(stat_data) + "\n"
            final.append(stat_line)
        stats.writelines(final)
    logger.info("Stats written")


def update_log(tweet_id, daynum, created_date, txt, web_attachment, image_attachment):
    formatted_date = created_date.split("T")[0]
    formatted_text = txt
    formatted_text = re.sub(
        "https://t.co/\w+\s*", "", formatted_text
    )  # remove twitter attachment links
    formatted_text = re.sub(
        r"([#@]\w+)", r"`\1`", formatted_text
    )  # wrap hashtags and mentions in blocks
    formatted_text = formatted_text.strip()
    daylog = f"""
## Day {daynum}: {formatted_date}

[Tweet](https://twitter.com/BudavariMatyas/status/{tweet_id})

**Today's Progress**: {formatted_text}

"""
    if ADD_THOUGHTS:
        daylog += """**Thoughts**:
"""
    if not web_attachment is None:
        daylog += f"""
**Link(s) to work**: [{web_attachment.get('title')}]({web_attachment.get('url')})
"""
    if not image_attachment is None:
        daylog += f"""
![{image_attachment.get('alt_text')}]({image_attachment.get('filepath')})
"""

    with open("../../log.md", "a") as lastday:
        lastday.write(daylog)


def main():
    last_day = get_last_visited_day()
    stat_data = []
    logger.info("Last visited day is: %d", last_day)
    for [daynum, id] in IDS:

        logger.info("Getting info for day: %d (id: %s)", daynum, id)
        tweet = get_tweet(id)

        txt = get_text(tweet)
        created_date = get_created_date(tweet)
        public_metrics = get_public_metrics(tweet)

        stat_data.append([id, daynum, created_date, public_metrics])
        # assuming we only add 1 new line at once
        if daynum <= last_day:
            continue
        # only update the text log, and get attachments for the last item
        web_attachment = get_web_attachment_url(tweet)
        image_attachment = download_image_attachment(daynum, tweet)
        update_log(id, daynum, created_date, txt, web_attachment, image_attachment)
        update_last_line(daynum)
    update_stats(stat_data)

    logger.info("DONE")


if __name__ == "__main__":
    main()
