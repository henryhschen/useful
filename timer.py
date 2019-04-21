#!/usr/local/bin/python3.6

import time, threading
from datetime import datetime

def cal_next_month ():
    now = datetime.now()
    next_month = list()
    timestamp = datetime.timestamp(now)
    now_str = str(now).split(" ")
    today = now_str[0].split("-")

    # identify year month day
    if(int(today[1]) != 12):
        next_month.append(today[0])
        next_month.append(str(int(today[1])+1))
        next_month.append(str(1))
    else:
        next_month.append(str(int(today[0])+1))
        next_month.append(str(1))
        next_month.append(str(1))
    next_month = "-".join(next_month)
    next_month = " ".join([next_month, "0:0:0.0"])
    next_month = datetime.strptime(next_month,"%Y-%m-%d %H:%M:%S.%f")
    until_month_sec = (next_month - now).total_seconds()
    print("From:", now, ", To:", next_month, "= ", next_month-now, " or Total second is", until_month_sec)
    return until_month_sec

def loop():
    until_month_sec = cal_next_month()
    threading.Timer(until_month_sec, loop).start()
loop() 
exit()
WAIT_SECONDS = 5

def foo():
    print("Event trigger start from", today)
    threading.Timer(WAIT_SECONDS, foo).start()
    
foo()

