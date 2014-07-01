__author__ = 'anouksha'

import pymongo
import re
import sys

db = pymongo.MongoClient().Twitter
tweets = db.tweets.find()
filename = "phone_stats"

phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})')
count = 0
pc = 0
for tweet in tweets:
    count += 1
    m = phonePattern.search(tweet['text'])
    if m:
        pc += 1
        #print str(pc)+". "+tweet['text'] + "\tNumber: "+ m.group()
        #print m.group()
        data={}
        data['name'] = tweet['user']['name']
        data['screen_name'] = tweet['user']['screen_name']
        data['created_at'] = tweet['created_at']
        data['timezone'] = tweet['user']['time_zone']
        data['text']=tweet['text']
        data['number'] = m.group()
        db.numbers.insert(data)


nums = db.numbers.distinct("number")
nc = 0
print "Distinct Numbers:"
for num in nums:
    nc += 1
    accounts =  (db.numbers.find({"number":num})).distinct("name")
    text = str(nc) +". " +num+"\tCount:"+str(db.numbers.find({"number":num}).count())+"\tNum of Accounts: "+str(len(accounts))
    try:
        output = open(filename,"a")
        output.write(text+"\n")
        output.close()
    except:
        pass

'''accounts =  (db.numbers.find({"number":"0881147035"})).distinct("name")
print str(len(accounts))'''
