__author__ = 'anouksha'

import pymongo

db = pymongo.MongoClient().Twitter

numbers_1 = db.numbers.find({"text":{"$regex":"[sS][Mm][Ss]/[Ww][Aa]"}}).sort([("count",pymongo.DESCENDING)]).distinct("number")
numbers_2 = db.numbers.find({"text":{"$regex":"[Ww]h[a]?ts[a]?pp"}}).sort([("count",pymongo.DESCENDING)]).distinct("number")
numbers = numbers_1 + list(set(numbers_2) - set(numbers_1))
print "Count:"+str(len(numbers))
for num in numbers:
    print num