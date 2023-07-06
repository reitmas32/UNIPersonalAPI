import datetime
import config as CONFIG

class TaskTime:
    hour = 8
    minute = 0

    def __init__(self, hour, minute) -> None:
        self.hour = hour
        self.minute = minute

class Job:
    hour: int
    minute: int
    task = None
    name: str

    task_times = []

    def hello():
        print('hello task')

    def __init__(self, name = 'default', task_times = [TaskTime(hour=8, minute=0)], task = hello) -> None:
        
        self.name = name
        self.task = task
        self.task_times = task_times

    def run_job(self):
        for task_time in self.task_times:
            if datetime.datetime.now().time().hour == task_time.hour and datetime.datetime.now().time().minute == task_time.minute :
                self.task()