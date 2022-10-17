from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
# import time
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)-8s %(message)s',
                    datefmt=r'%Y-%m-%d %H:%M:%S',
                    filename=datetime.datetime.now().strftime(r'%Y-%m-%d %H:%M:%S') + '.log',
                    filemode='a')

def listener(event):
    if event.exception:
        print("Error occured!")
    else:
        print("Tasks running..")

def error_job(): # for testing only
    print(1/0)

def interval_task():
    executors = {
        'default': ThreadPoolExecutor(10)
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 2
    }
    sched = BlockingScheduler(executors=executors, job_defaults=job_defaults)
    sched.add_job(error_job, next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id="error_job")
    sched.add_job(interval_job, "interval", id="interval_task", seconds=10)

    sched.add_listener(listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    sched._logger = logging

    sched.start()

def interval_job():
    print("The time is %s"%datetime.datetime.now())

# sched.start()
if __name__ == '__main__':
    interval_task()

