import twitter
from config import TWITTER_KEYS
from tmp_base import USERS
import json
import os

TAPI = twitter.Api(**TWITTER_KEYS)
CWD = '/home/karol/workspace/nlp/'


def save_tweets(tweets: list, filename: str = "tweets.json"):
    filepath = os.path.join(CWD, 'resources/', filename)
    with open(filepath, "w") as outfile:
        json.dump(tweets, outfile)


def get_tweets_from_users(users: list):
    all_tweets = []
    for user in users:
        timeline = TAPI.GetUserTimeline(screen_name=user, count=15)
        for tweet in timeline:
            all_tweets.append(tweet.text)
            print(tweet.id, tweet.text)
    save_tweets(all_tweets)


if __name__ == '__main__':
    get_tweets_from_users(USERS)
