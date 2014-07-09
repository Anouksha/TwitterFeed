__author__ = 'anouksha'

import pymongo
import re
import sys

db = pymongo.MongoClient().tweets
tweets = db.bharat_phonetweets.find(timeout=False)


phonePattern = re.compile(r'[+]?([0-9]+)?[\(.*=$,~ \n\t-]?\s*(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*\(?(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*(\d{4})\d*')
count = 0
pc = 0
for tweet in tweets:
    pc += 1
    if pc > 175279:
        m = phonePattern.search(tweet['text'])
        if m:
            #pc += 1
            #print str(pc)+". "+tweet['text'] + "\tNumber: "+ m.group()
            #print m.group()
            number = m.group().strip()
            data={}
            data['name'] = tweet['user']['name']
            data['screen_name'] = tweet['user']['screen_name']
            data['created_at'] = tweet['created_at']
            data['timezone'] = tweet['user']['time_zone']
            data['text']=tweet['text']
            data['verified'] = tweet['user']['verified']
            data['number'] = number
            db.bharat_numbers.insert(data)

            c = db.bharat_phone_stats.find({"number": number}).count()
            if c>0:
                num = db.bharat_phone_stats.find({"number": number})
                for n in num:
                    count = n['count'] + 1
                    accounts = (db.bharat_numbers.find({"number": number})).distinct("name")
                    db.bharat_phone_stats.update({"number": number},{"$set": {"count": count, "accounts": accounts, "accounts_num":len(accounts)}})

            else:
                data2 = {}
                accounts = (db.bharat_numbers.find({"number":number})).distinct("name")
                data2['number'] = number
                data2['count'] = db.bharat_numbers.find({"number":number}).count()
                data2['accounts'] = accounts
                data2['accounts_num'] = len(accounts)
                db.bharat_phone_stats.insert(data2)

        else:
            data={}
            data['name'] = tweet['user']['name']
            data['screen_name'] = tweet['user']['screen_name']
            data['created_at'] = tweet['created_at']
            data['timezone'] = tweet['user']['time_zone']
            data['text']=tweet['text']
            data['verified'] = tweet['user']['verified']
            data['number'] = "no match"
            db.bharat_numbers.insert(data)

tweets.close()