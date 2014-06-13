__author__ = 'anouksha'

import tweepy
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

    def __init__(self,api):
        self.count = 0
        self.api=api

    '''def on_data(self, data):

        print data
        self.db = pymongo.MongoClient().test
        self.db.thousand_tweets.insert(json.loads(data))
        return True'''

    '''def on_status(self, status):
        phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
        m = phonePattern.search(status.text)
        if m:
            #self.db = pymongo.MongoClient().test
            #self.db.phonetweets.insert(json.loads(status.text))
            #print str(status.created_at)+ str(status.user.time_zone)+"          "+status.user.name
            #print status.text+"\t"+ m.group()
            print status
            data={}
            data['text']=status.text
            db = pymongo.MongoClient().test
            db.phonetweets.insert(data)'''

    def on_status(self, status):
        phonePattern = re.compile(r'(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*(\d{1})\D*$')
        m = phonePattern.search(status.text)
        if m:
            self.count += 1
            print str(self.count)+". "+status.text
            data={}
            data['text']=status.text
            db = pymongo.MongoClient().sample
            db.hundred_tweets.insert(data)
            if self.count>=100:
                exit()


    def on_error(self, status):
        print status


auth=OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
l=listener(tweepy.API(auth))
twitterStream = Stream(auth, l)
try:
    twitterStream.filter(track=["call","dial", "sms", "contact number","text"])
except:
    pass




