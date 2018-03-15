#!/usr/bin/python

#import time
import pyb

def now():
    return pyb.millis()

class Job:
    def __init__(self, period, callback):
        self.callback = callback
        self.period = period
        self.next_run = now()+period

    def run(self):
        ret = self.callback()
        self.next_run += self.period
        return ret

class Scheduler:
    def __init__(self):
        self.jobs = []

    def run_pending(self):
        for job in self.jobs:
            if now() > job.next_run:
                job.run()

    def clear(self):
        self.jobs = []

    def add_job(self ,period, callback):
        self.jobs.append(Job(period,callback))


if __name__ == "__main__":

    scheduler = Scheduler()
    scheduler.add_job(1, lambda :print('coucou'))
    scheduler.add_job(5, lambda :print('coucou2'))
    scheduler.add_job(1, lambda :print('coucou3'))
    scheduler.add_job(2, lambda :print('coucou4'))

    while True:
        time.sleep(0.01)
        scheduler.run_pending()
