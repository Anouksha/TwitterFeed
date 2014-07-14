import pymongo
import re

db = pymongo.MongoClient().Twitter

'''nums = db.phone_stats.find()

for n in nums:
	if n['count']>1000:
		print n['number']+"\tCount: "+str(n['count'])'''

nums = db.phone_stats.find().sort([("count", pymongo.DESCENDING), ("accounts_num", pymongo.DESCENDING)]).limit(100)
print "Number\tRetweets\tTotal_Count\tVerified\tNot_verified\tTotal_Accounts"
for n in nums:
    try:
        rt_count = 0
        no_rt_count = 0
        verified = len(db.numbers.find({"verified": True, "number": n['number']}).distinct("name"))
        not_verified = len(db.numbers.find({"verified": False, "number": n['number']}).distinct("name"))
        pattern=re.compile(n['number'])
        #print n['number']
        rt_count += db.tweets.find({"text": {"$regex":pattern}, "retweet_count": {"$gt": 0}}).count()
        #print str(rt_count)

        '''data = (db.tweets.find({"text": {"$regex": pattern}, "retweeted_status.retweet_count": {"$gt": 0}}).sort([("retweeted_status.retweet_count", pymongo.DESCENDING)]).limit(1))
        for d in data:
            rt_count += d['retweeted_status']['retweet_count']'''
        #no_rt_count += db.tweets.find({"text": {"$regex":pattern}, "retweet_count": 0}).count()
        #print no_rt_count
        rt_count += db.tweets.find({"text": {"$regex": pattern}, "retweeted_status.retweet_count": {"$gt": 0}}).count()
        print n['number'] + "\t" + str(rt_count) + "\t" + str(n['count']) + "\t" + str(verified) + "\t" + str(not_verified) + "\t" + str(n['accounts_num'])
    except:
        pass
'''pattern = re.compile('^[+]?[1]?[4][4][1]')

nums = db.phone_stats.find()

for n in nums:
	if pattern.search(n['number']):
		print n['number'] + "\tCount: "+str(n['count'])'''

print "Done"
