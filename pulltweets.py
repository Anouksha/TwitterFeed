__author__ = 'anouksha'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re
import json
import pymongo

api_key = 'ARuQQNlhwQPF8X1zHbbQOGkJW'
api_secret = 'IboCMM6EjsBqaUlD2vLe4Crr1OtaDp58btKiYd7loUUTvDiUQM'
access_token = '2536032672-a5X8UEDQhZxsaHHjYPcUmtQbuVfDlw27pPF89xp'
access_secret = 'fQaBw3TG9K8eoMtV0MtBERJhCJJw1gBRY8aPaMtnqe1Qg'

count=1

class listener(StreamListener):


    '''def on_data(self, data):

        #print data
        self.db = pymongo.MongoClient().test
        self.db.tweets.insert(json.loads(data))
        return True'''

    def on_status(self, status):
        phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        m = phonePattern.search(status.text)
        if m:
            #self.db = pymongo.MongoClient().test
            #self.db.phonetweets.insert(json.loads(status.text))
            print str(status.created_at)+ str(status.user.time_zone)+"          "+status.user.name
            #print status.text+"\t"+ m.group()
            '''data={}
            data['text']=status.text
            db = pymongo.MongoClient().test
            db.phonetweets.insert(data)'''

    def on_error(self, status):
        print status


auth=OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
l=listener()
twitterStream = Stream(auth, l)
twitterStream.filter(track=["call", "text","dial"])


