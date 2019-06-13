import twitter
from ..config import TWITTER_KEYS
import json
import os

TAPI = twitter.Api(**TWITTER_KEYS)
CWD = './'


def save_tweets(tweets: list, filename: str = "tweets2.json"):
    filepath = os.path.join(CWD, filename)
    with open(filepath, "w+") as outfile:
        json.dump(tweets, outfile)


def is_tweet_valuable(tweet):
    tweet_full_text = tweet.text
    urls_concatenated = ""

    for url in tweet.urls:
        urls_concatenated += url.url
    if not len(tweet_full_text) - len(urls_concatenated) > 30:
        return False

    return True


def find_user_tweets(user):
    return TAPI.GetUserTimeline(screen_name=user, count=30)
