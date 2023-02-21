import datetime
import time

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)
