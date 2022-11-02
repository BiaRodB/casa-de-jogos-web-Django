
import time
from random import randint, sample 
import random
import sched
from sched import scheduler
scheduler = sched.scheduler

def job():
     formB = sample(range(0,9),4)
     scheduler.enter(delay=5,priority=0,action=job)

job()

#sched.scheduler
#scheduler.run(job)
#schedule.every().day.at("20:00").do(job)
#scheduler.every().monday.do(job)
#scheduler.every().wednesday.at("13:15").do(job)
#scheduler.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)