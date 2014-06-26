__author__ = 'anouksha'

import json
import pymongo
from os import listdir

db = pymongo.MongoClient().tweets
path = '/home/bharat/data/twitter'
count = 0

#This for loop will iterate through each file in the directory

for f in listdir(path):

  '''The for loop below will read each line of the file and attempt to parse the tweet data
  using json.loads(), a function that converts raw JSON messages into objects. '''

  count = count + 1
  if count > 373:
    tweets=[]
    filepath = path+'/'+f
    print str(count) + ". "+filepath
    for line in open(filepath):
      try:
        tweets.append(json.loads(line))
      except:
        pass

    #storing each tweet into the bharat_phonetweets collection in the tweets DB
    for tweet in tweets:
      #print tweet
      #db = pymongo.MongoClient().tweets
      db.bharat_phonetweets.insert(tweet)
 
print "Done"
