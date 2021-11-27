import time
from datetime import datetime
while True:
    today = datetime.now()
    xmas = datetime(2021,12,25,0,0,0)
    timeleft = xmas - today
    print("Countdown to Xmas 2021: ",timeleft)
    time.sleep(5)