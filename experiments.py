from data_algorithms import nlp
from twitterapi import twitter_api
from tmp_base import USERS
from tmp_touristic_proposals import PROPOSALS
from collections import defaultdict

def analyze_db_users():
    categories_of_tweets = defaultdict(list)
    for user in USERS:
        tweets = twitter_api.get_tweets_from_user(user)
        for tweet in tweets:
            categories_of_tweets[user].append(nlp._get_categories_from_text(tweet))

    print(0)
analyze_db_users()
