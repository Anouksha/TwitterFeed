__author__ = 'anouksha'

import json
import pymongo


tweets = []

'''The for loop below will read each line of the file and attempt to parse the tweet data
 using json.loads(), a function that converts raw JSON messages into objects. '''

for line in open('/home/anouksha/Documents/Special Problem/phone.20140414-034737.json'):
  try:
    tweets.append(json.loads(line))
  except:
    pass

#storing each tweet into the bharat_phonetweets collection in the sample DB
for tweet in tweets:
    #print tweet
    db = pymongo.MongoClient().sample
    db.bharat_phonetweets.insert(tweet)