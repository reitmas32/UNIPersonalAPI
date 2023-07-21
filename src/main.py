import datetime
from models.job import Job, TaskTime
import time

from jobs.hapybirth_day import felicitar_cumple
from jobs.load_personal import load_personal

import config as CONFIG

def hola_message():
    CONFIG.bot.send_message(CONFIG.GROUP_ID, f'Hola: {datetime.datetime.now()}')

def generate_cron_task_times(minute_time_step):
    task_times = []
    for hour in range(24):
        for minute in range(0, 60, minute_time_step):
            task_times.append(TaskTime(hour=hour, minute=minute))
    return task_times

def main():

    list_jobs = []

    CONFIG.DELTA_ZONE = -1

    
    list_jobs.append(

        Job(name='Load Personal', task=load_personal, task_times=[
            TaskTime(hour=7, minute=30),
            TaskTime(hour=8, minute=50),
            ]
        )
    )
    list_jobs.append(

        Job(name='Load Personal', task=felicitar_cumple, task_times=[
            TaskTime(hour=8, minute=0),
            TaskTime(hour=9, minute=0),
            ]
        )
    )
    
    while True:
        for job in list_jobs:
            job.run_job()
        time.sleep(60)

main()