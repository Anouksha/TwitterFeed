__author__ = 'anouksha'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re
import pymongo
import json
import time

api_key = 'ARuQQNlhwQPF8X1zHbbQOGkJW'
api_secret = 'IboCMM6EjsBqaUlD2vLe4Crr1OtaDp58btKiYd7loUUTvDiUQM'
access_token = '2536032672-a5X8UEDQhZxsaHHjYPcUmtQbuVfDlw27pPF89xp'
access_secret = 'fQaBw3TG9K8eoMtV0MtBERJhCJJw1gBRY8aPaMtnqe1Qg'

class listener(StreamListener):

    '''def __init__(self):
        self.count = 1
        #self.api=api
        self.filename = "phone-"+time.strftime('%d-%m-%Y:%H:%M:%S')
        self.text=""
        #self.output = open(self.filename, 'a')'''

    def on_data(self, data):

        phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        m = phonePattern.search(json.loads(data)['text'])
        if m:
            print json.loads(data)['text']
            #print status
            db = pymongo.MongoClient().tweets
            db.phone_numbers.insert(json.loads(data))
            #output = open(self.filename, 'a')
            '''self.text = self.text+str(self.count)+". "+json.loads(data)['text']
            print str(self.count)+". "+json.loads(data)['text']
            self.count += 1'''
        return True

    def on_error(self, status):
        print status

    '''def write_data(self, text):
        output = open(self.filename, 'a')
        output.write(text+"\n")
        output.close()'''


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
    #l.write_data(l.text)
except:
    pass