__author__ = 'anouksha'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re
import pymongo
import json
import time
import datetime
import sched

api_key = 'ARuQQNlhwQPF8X1zHbbQOGkJW'
api_secret = 'IboCMM6EjsBqaUlD2vLe4Crr1OtaDp58btKiYd7loUUTvDiUQM'
access_token = '2536032672-a5X8UEDQhZxsaHHjYPcUmtQbuVfDlw27pPF89xp'
access_secret = 'fQaBw3TG9K8eoMtV0MtBERJhCJJw1gBRY8aPaMtnqe1Qg'

class listener(StreamListener):

    def __init__(self):
        self.count = 0
        self.sec = 1
        #self.api=api
        #self.filename = "phone-"+time.strftime('%d-%m-%Y:%H:%M:%S')
        self.filename = "statistics"
        self.start_time = datetime.datetime.now()
        #self.output = open(self.filename, 'a')

    def on_data(self, data):

        phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        m = phonePattern.search(json.loads(data)['text'])
        if m:
            #print json.loads(data)['text']
            #print status
            #db = pymongo.MongoClient().tweets
            #db.phone_numbers.insert(json.loads(data))
            try:

                self.count += 1
                text = str(self.count)+". "+json.loads(data)['text']
                print text
                t=datetime.datetime.now()
                if (t-self.start_time) > datetime.timedelta(0,30):
                    output = open(self.filename, 'a')
                    output.write(time.strftime('%d-%m-%Y:%H:%M:%S')+"\t"+str(self.sec)+"\t"+str(self.count)+"\n")
                    self.count = 0
                    self.sec += 1
                    self.start_time = datetime.datetime.now()
                    output.close()
            except:
                pass
            '''finally:
                output.close()'''
            #    s=sched.scheduler(time.time, time.sleep)
            #    s.enter(20,1,self.write_data,(s,))
            #    s.run()
        return True

    '''def write_data(self, sc):
        output = open(self.filename, 'a')
        output.write(time.strftime('%d-%m-%Y:%H:%M:%S')+"\t"+self.sec+"\t"+self.count+"\n")
        output.close()
        self.count = 1
        self.sec += 1
        sc.enter(20,1,self.write_data,(sc,))'''

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

