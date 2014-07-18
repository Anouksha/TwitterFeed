__author__ = 'anouksha'

import datetime
import pymongo
import json

today = datetime.datetime.now()
yest = today - datetime.timedelta(days =7)
datePattern = yest.strftime("^%a %b %d.*%Y")
print datePattern
db = pymongo.MongoClient().Twitter
tweets = db.tweets.find({"created_at":{"$regex":datePattern}})
#print tweets
count = tweets.count()
print count
limit = int(count/10) + 1
#print limit
c = 0
file = 1
filename = "tweets_"
output = open(filename+str(file), 'a')
for tweet in tweets:
    #print tweet
    del tweet['_id']
    c += 1
    if c <= limit:
        output.write(json.dumps(tweet)+"\n")
        #output.write("\n")
    else:
        c = 0
        file += 1
        output.close()
        output = open(filename+str(file), 'a')

output.close()
print "Done"