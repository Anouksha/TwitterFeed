__author__ = 'anouksha'

import pymongo
import sys

db = pymongo.MongoClient().Twitter
timezones = db.numbers.distinct("timezone")

print "Total number of distinct timezones: "+str(len(timezones))
timezones = sorted(timezones)
for t in timezones:
    try:
        count = db.numbers.find({"timezone":t}).count()
        print t+"\t\t"+str(count)
    except:
        sys.exc_info()
