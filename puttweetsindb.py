__author__ = 'anouksha'

import json
import pymongo


tweets = []

for line in open('/home/anouksha/Documents/Special Problem/phone.20140414-034737.json'):
  try:
    tweets.append(json.loads(line))
  except:
    pass

for tweet in tweets:
    #print tweet
    db = pymongo.MongoClient().sample
    db.bharat_phonetweets.insert(tweet)