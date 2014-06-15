__author__ = 'anouksha'

import pymongo

db = pymongo.MongoClient().sample
tweets = db.hundred_tweets.find()

for tweet in tweets:
    print tweet['text']
