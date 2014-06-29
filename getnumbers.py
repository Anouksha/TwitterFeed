__author__ = 'anouksha'

import pymongo
import re
import sys

db = pymongo.MongoClient().tweets
tweets = db.phone_numbers.find()
filename = "phone_stats"

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})')
count = 0
pc = 0
for tweet in tweets:
    count += 1
    if count <= 100:
        m = phonePattern.search(tweet['text'])
        if m:
            pc += 1
            print str(pc)+". "+tweet['text'] + "\tNumber: "+ m.group()
            data={}
            data['name'] = tweet['user']['name']
            data['screen_name'] = tweet['user']['screen_name']
            data['created_at'] = tweet['created_at']
            data['timezone'] = tweet['user']['time_zone']
            data['text']=tweet['text']
            data['number'] = m.group()
            db.numbers.insert(data)


tweets_2 = db.numbers.find()

nums = db.numbers.distinct("number")
nc = 0
print "Distinct Numbers:"
for num in nums:
    nc += 1
    print str(nc) +". " +num+"\tCount:"+str(db.numbers.find({"number":num}).count())