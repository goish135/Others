from apscheduler.schedulers.blocking import BlockingScheduler
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=15 , minute=20)
def scheduled_job():
    print('you can be better.')
    os.system("python dcard_and_sendmail.py")
sched.start()