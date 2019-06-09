import twitter
from config import TWITTER_KEYS
import json
import os

TAPI = twitter.Api(**TWITTER_KEYS)
CWD = './'


def save_tweets(tweets: list, filename: str = "tweets2.json"):
    filepath = os.path.join(CWD, filename)
    with open(filepath, "w+") as outfile:
        json.dump(tweets, outfile)

def find_user_tweets(user):
    return TAPI.GetUserTimeline(screen_name=user, count=30)

