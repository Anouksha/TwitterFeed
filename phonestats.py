__author__ = 'anouksha'

import pymongo
import re

db = pymongo.MongoClient().tweets

nums = db.numbers.distinct("number")
nc = 0
print "Distinct Numbers:"
for num in nums:
    nc += 1
    accounts =  (db.numbers.find({"number":num})).distinct("name")
    #text = str(nc) +". " +num+"\tCount:"+str(db.numbers.find({"number":num}).count())+"\tNum of Accounts: "+str(len(accounts))
    data = {}
    data['number'] = num
    data['count'] = db.numbers.find({"number":num}).count()
    db.phone_stats.insert()