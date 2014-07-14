import pymongo
import re

db = pymongo.MongoClient().Twitter

'''nums = db.phone_stats.find()

for n in nums:
	if n['count']>1000:
		print n['number']+"\tCount: "+str(n['count'])'''

'''nums = db.phone_stats.find().sort([("count",pymongo.DESCENDING),("accounts_num",pymongo.DESCENDING)]).limit(150)

for n in nums:
	print n['number']+"\t"+str(n['count'])+"\t"+str(n['accounts_num'])'''


pattern = re.compile('^[+]?[1]?[4][4][1]')

nums = db.phone_stats.find()

for n in nums:
	if pattern.search(n['number']):
		print n['number'] + "\tCount: "+str(n['count'])

print "Done"
