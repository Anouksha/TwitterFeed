__author__ = 'anouksha'

import tweepy
from tweepy import OAuthHandler
from tweepy import TweepError
import pymongo
import sys

api_key = 'HU4NnHMfgMaWWl9yvwyUZ6ngO'
api_secret = 'xfkf2Kzno8leUjCT7MoFR7G1348yzdFKNjw1Fby074c9IShUKY'
access_token = '2536032672-WZiuBZf2NenQC4q5ulnBDu8NtRO5WlBBOTF01Bh'
access_secret = 'K77q99T28ecB5ERtkfFedtW6K0ikVBmkwiNYwikGooXlH'

auth=OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

db = pymongo.MongoClient().tweets
users = db.numbers.distinct("screen_name")
active = 0

print "Total Number of Accounts: "+str(len(users))
for u in users:
    try:
        user = api.get_user(screen_name=u)
        active += 1
        print u+": Active Account"
    except TweepError as error:
        if error.message[0]['code'] == 63:
            print u+": User has been suspended"
        print sys.exc_info()
    except:
        print sys.exc_info()

print "Total No. of Active Accounts: "+str(active)