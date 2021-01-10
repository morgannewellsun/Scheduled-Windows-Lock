import ctypes
import datetime
import os
import psutil
import time

SCHEDULE = {
    0: [0, 500],
    1: [0, 500],
    2: [0, 500],
    3: [0, 500],
    4: [0, 500],
    5: None,
    6: None,
}

current_pid = os.getpid()
try:
    with open("lockfile.txt", "r") as lockfile:
        most_recent_pid = int(lockfile.read())
        if psutil.pid_exists(most_recent_pid):
            exit()
except FileNotFoundError:
    pass

with open("lockfile.txt", "w") as lockfile:
    lockfile.write(str(current_pid))
while True:
    day_of_week = datetime.datetime.today().weekday()
    if SCHEDULE[day_of_week] is not None:
        time_of_day = datetime.datetime.today().hour * 100 + datetime.datetime.today().minute
        if SCHEDULE[day_of_week][0] <= time_of_day < SCHEDULE[day_of_week][1]:
            ctypes.windll.user32.LockWorkStation()
    time.sleep(1)

