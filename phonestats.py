__author__ = 'anouksha'

import pymongo
import re

db = pymongo.MongoClient().Twitter

nums = db.numbers.distinct("number")
nc = 0

for num in nums:
    if num != "no match":
        nc += 1
        accounts =  (db.numbers.find({"number":num})).distinct("name")
        #text = str(nc) +". " +num+"\tCount:"+str(db.numbers.find({"number":num}).count())+"\tNum of Accounts: "+str(len(accounts))
        data = {}
        data['number'] = num
        data['count'] = db.numbers.find({"number":num}).count()
        data['accounts'] = accounts
        data['accounts_num'] = len(accounts)
        db.phone_stats.insert(data)

print "Distinct Numbers: "+str(nc)