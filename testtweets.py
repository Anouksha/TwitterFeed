__author__ = 'anouksha'

import pymongo
import re

db = pymongo.MongoClient().sample
tweets = db.hundred_tweets.find()

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
count = 1
for tweet in tweets:
    #print tweet['text']
    if phonePattern.search(tweet['text']):
        print str(count)+". "+tweet['text']
    count +=1