__author__ = 'anouksha'

'''from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

def job_function():
    print "Hello World"


sched.add_cron_job(job_function, second = '*/10')'''

import time
import sched

def job__function(sc):
    print time.strftime('%d-%m-%Y:%H:%M:%S')+"\tHello World"
    sc.enter(10,1,job__function,(sc,))

print "Outside"
s=sched.scheduler(time.time, time.sleep)
s.enter(10,1,job__function,(s,))
s.run()



'''from crontab import CronTab

cron = CronTab()
cmd = 'sudo ~/PycharmProjects/TwitterFeed/./my_script.sh'
job  = cron.new(cmd)
job.minute.every(2)
cron.remove_all()
cron.write()

print cron.render()'''