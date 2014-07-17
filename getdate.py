__author__ = 'anouksha'

import datetime
import pymongo
import time
import re

'''db = pymongo.MongoClient().Twitter
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
        print 'Not there'''

today = datetime.datetime.now()
yest = today - datetime.timedelta(hours =24)
datePattern = yest.strftime("^%a %b %d.*%Y")
print datePattern
db = pymongo.MongoClient().Twitter
tweets = db.tweets.find({"created_at":{"$regex":datePattern}}).count()
print tweets

'''for tweet in tweets:
    print tweet'''