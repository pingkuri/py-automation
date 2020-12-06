import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError



def job():
    print("I'm working...", "| [time] "
          , str(time.localtime().tm_hour) + ":"
          + str(time.localtime().tm_min) + ":"
          + str(time.localtime().tm_sec))


def job_2():
    print("Job2 실행: asd  ", "| [time] "
          , str(time.localtime().tm_hour) + ":"
          + str(time.localtime().tm_min) + ":"
          + str(time.localtime().tm_sec))

sched = BackgroundScheduler()
sched.start()


# every 3 seconds
sched.add_job(job, 'interval', seconds=3, id="test_2")  

# using cron, every 5 seconds
sched.add_job(job, 'cron', second='*/5', id="test_1")

# every HH:59:10
sched.add_job(job_2, 'cron', minute="59", second='10', id="test_10")



while True:
    print("Running main process...............")
    time.sleep(1)