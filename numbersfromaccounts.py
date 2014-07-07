__author__ = 'anouksha'

import pymongo
import sys

db = pymongo.MongoClient().Twitter
users = db.numbers.distinct("screen_name")

for u in users:
    try:
        numbers = db.numbers.find({"screen_name":u}).distinct("number")
        print u+"\tNumbers: "+str(len(numbers))
    except:
        print sys.exc_info()