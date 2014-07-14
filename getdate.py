__author__ = 'anouksha'

import datetime
import pymongo
import time

db = pymongo.MongoClient().Twitter
tweets = db.tweets.find()
dates =[]
for tweet in tweets:
    dates.append(tweet['created_at'])

today = datetime.datetime.now()

for d in dates:
    #print time.strftime('%d-%m-%Y:%H:%M:%S',time.strptime(d,"%a %b %d %H:%M:%S +0000 %Y"))
    t = time.strptime(d,"%a %b %d %H:%M:%S +0000 %Y")
    if t.tm_mday == today.day and t.tm_year == today.year and t.tm_mon == today.month:
        print t
    else:
        print 'Not there'