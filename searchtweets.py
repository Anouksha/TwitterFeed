__author__ = 'anouksha'

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re
import json
import pymongo
import urllib, urllib2

api_key = 'ARuQQNlhwQPF8X1zHbbQOGkJW'
api_secret = 'IboCMM6EjsBqaUlD2vLe4Crr1OtaDp58btKiYd7loUUTvDiUQM'
access_token = '2536032672-a5X8UEDQhZxsaHHjYPcUmtQbuVfDlw27pPF89xp'
access_secret = 'fQaBw3TG9K8eoMtV0MtBERJhCJJw1gBRY8aPaMtnqe1Qg'

auth=OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

results = api.search(q="dial")
count = 1
for result in results:
    if phonePattern.search(result.text):
        print str(count)+'. '+result.text
        count+=1
        data={}
        data['text']=result.text
        db = pymongo.MongoClient().test
        db.phonetweets.insert(data)

'''def search_twitter(query, no_retweets=True):
    if no_retweets:
        query += ' -RT'

    url = 'http://search.twitter.com/search.json?%s' % urllib.urlencode({
            'q': query,
            'lang': 'en', # restrict results to english tweets
            'rpp': 100, # return 100 results per page (maximum value)
    })
    response = json.loads(urllib2.urlopen(url).read())
    return response['results']


results = search_twitter('call')

for tweet in results:
    print tweet['text'].encode('utf-8', 'ignore')'''