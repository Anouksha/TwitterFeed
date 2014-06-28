__author__ = 'anouksha'

import pymongo
import re

db = pymongo.MongoClient().sample
tweets = db.hundred_tweets.find()

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})')
#phonePattern = re.compile('(([+]?([0-9]+)[.*=$, \n\t-])?\\s*\\(?\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*\\)?\\s*[.*=$, \n\t-]\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*[.*=$, \n\t-]\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*([0-9]))')
count = 1
for tweet in tweets:
    #print tweet['text']
    if phonePattern.search(tweet['text']):
        print str(count)+". "+tweet['text'] + "\tNumber: "+ phonePattern.search(tweet['text']).group()
        count +=1