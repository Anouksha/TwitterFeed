__author__ = 'anouksha'

import re

count = 0
sum = 0
pattern = re.compile(r'Count: ')
filename = "hourly_stats"

for line in open("statistics"):
    count += 1
    m = pattern.search(line)
    if m:
        length = len(line)
        index = length - m.end()
        num = line[-index:]
        c = num[:-1]
        #print c
        sum = sum + int(c)
        if count % 4 == 0:
            #print sum
            try:
                output = open(filename,'a')
                output.write(str(sum)+"\n")
                output.close()
            except:
                pass
            sum = 0


print "Total Count: "+str(count)