# tester:v1.0.0

from time import sleep
import os
from datetime import datetime

def time_pid():
    pid = os.getpid()
    current_time = datetime.now()
    date_time = current_time.strftime("%Y/%m/%d/%H:%M:%S")
    output = date_time + '/' + str(pid)
    return output

for _ in range(10):
    print(time_pid())
    sleep(0.5)