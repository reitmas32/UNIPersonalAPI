import datetime
from models.job import Job, TaskTime
import time

from jobs.hapybirth_day import felicitar_cumple
from jobs.load_personal import load_personal

import config as CONFIG

def main():

    list_jobs = []

    CONFIG.DELTA_ZONE = -1

    list_jobs.append(
        Job(name='Happy BirthDay', task=felicitar_cumple, task_times=[
            TaskTime(hour=17, minute=0),
            ]))
    list_jobs.append(

        Job(name='Load Personal', task=load_personal, task_times=[
            TaskTime(hour=16, minute=59),
            ]
        )
    )
    while True:
        for job in list_jobs:
            job.run_job()
        time.sleep(60)
main()