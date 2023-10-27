import datetime
import time

while True:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    hour_str = f"{hour:02d}"
    minute_str = f"{minute:02d}"
    second_str = f"{second:02d}"

    clock = f"{chr(16)} ► {hour_str}:{minute_str}:{second_str} ◄ {chr(17)}"

    print(clock, end='\r', flush=True)

    time.sleep(0.5)