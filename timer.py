

import schedule
import time

def job():
    print('Im working')

def twenty():
    print('Its been 20 seconds')

schedule.every(3).seconds.do(job)
schedule.every(20).seconds.do(twenty)


while 1:
    schedule.run_pending()
