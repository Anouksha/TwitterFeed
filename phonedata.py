__author__ = 'anouksha'

import pymongo

db = pymongo.MongoClient().Twitter

counts = db.phone_stats.distinct("count")
counts = sorted(counts)
filename = "count_data"

#print counts
try:
    output = open(filename,"a")
    output.write("No. of Phone#"+"\t \t"+"Count"+"\n")
    output.close()
except:
    pass

for c in counts:
    try:
        text = str(db.phone_stats.find({"count":c}).count())+"\t\t\t\t\t"+ str(c)
        output = open(filename,"a")
        output.write(text+"\n")
        output.close()
    except:
        pass