__author__ = 'anouksha'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re
import pymongo
import json
import time
import datetime
import sys

api_key = 'ARuQQNlhwQPF8X1zHbbQOGkJW'
api_secret = 'IboCMM6EjsBqaUlD2vLe4Crr1OtaDp58btKiYd7loUUTvDiUQM'
access_token = '2536032672-a5X8UEDQhZxsaHHjYPcUmtQbuVfDlw27pPF89xp'
access_secret = 'fQaBw3TG9K8eoMtV0MtBERJhCJJw1gBRY8aPaMtnqe1Qg'

class listener(StreamListener):

    def __init__(self):
        self.count = 0
        self.hour = 1
        #self.api=api
        self.filename = "statistics"
        self.start_time = datetime.datetime.now()
        #self.output = open(self.filename, 'a')

    def on_data(self, data):

        phonePattern = re.compile(r'[+]?([0-9]+)?[\(.*=$,~ \n\t-]?\s*(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*\(?(\d{3})\s*\)?[\\\/.*=$,~ \n\t-]?\s*(\d{4})\d*')
        m = phonePattern.search(json.loads(data)['text'])
        if m:
            try:
                self.count += 1
                #text = str(self.count)+". "+json.loads(data)['text']
                #print text
                #print status
                db = pymongo.MongoClient().Twitter
                db.tweets.insert(json.loads(data))
                data1={}
                data1['name'] = json.loads(data)['user']['name']
                data1['screen_name'] = json.loads(data)['user']['screen_name']
                data1['created_at'] = json.loads(data)['created_at']
                data1['timezone'] = json.loads(data)['user']['time_zone']
                data1['text']=json.loads(data)['text']
                data1['number'] = m.group().strip()
                db.numbers.insert(data1)

                t=datetime.datetime.now()
                if (t-self.start_time) > datetime.timedelta(0, 59, 0, 0, 14, 0, 0):
                    output = open(self.filename, 'a')
                    output.write(time.strftime('%d-%m-%Y:%H:%M:%S')+"\tCount: "+str(self.count)+"\n")
                    self.count = 0
                    self.hour += 1
                    self.start_time = datetime.datetime.now()
                    output.close()
                    raise SystemExit
            except Exception:
                pass
        return True

    def on_error(self, status):
        print status


auth=OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
l=listener()
twitterStream = Stream(auth, l)
try:
    twitterStream.filter(track=["call", "text","dial","credit","card","services", "caller","interest",
                            "mortgage","insurance","calling","scam","political","company", "visa",
                            "rate", "cash","sales","phone","loan","marketing","sms","law","free",
                            "cell","security","number","visa","contact","800notes", "telemarketer",
                            "yellowpages","yellowpage", "fraud", "customer service", "landline",
                            "toll-free", "toll free", "complaint", "complaints", "tele", "cell phone",
                            "1-800","1-866","1-888","fax", "voice", "land line", "mobile", "ext"])
except:
    pass
