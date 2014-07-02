__author__ = 'anouksha'

import pymongo
import re

db = pymongo.MongoClient().sample
tweets = db.hundred_tweets.find()

phonePattern = re.compile(r'[+]?([0-9]+)?[\(.*=$,~ \n\t-]?\s*(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*\(?(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*(\d{4})\d*')
#phonePattern = re.compile('(([+]?([0-9]+)[.*=$, \n\t-])?\\s*\\(?\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*\\)?\\s*[.*=$, \n\t-]\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*[.*=$, \n\t-]\\s*([0-9])\\s*([0-9])\\s*([0-9])\\s*([0-9]))')
count = 1
for tweet in tweets:
    #print tweet['text']
    if phonePattern.search(tweet['text']):
        print str(count)+". "+tweet['text'] + "\tNumber: "+ phonePattern.search(tweet['text']).group()
    count +=1