import datetime
import time

now = datetime.datetime.now()
minute = ''

while(True):
    print(minute)
    if (now.minute < 10):
        minute = f"0{now.minute}"
    print(minute)
    time.sleep(5)
