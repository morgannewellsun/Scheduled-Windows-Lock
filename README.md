# Scheduled-Windows-Lock

In hopes of better enforcing my bedtime habits, I needed a simple program that would automatically lock my Windows desktop on a schedule.

The schedule is defined in `scheduled_lock.py` by the `SCHEDULE` dictionary, which allows you to specify a different start and end time for each day of the week.

While the computer is supposed to be "locked", the script will continuously lock the workstation screen, preventing computer use.

A lockfile is created to ensure that only one instance of this script runs at any given time; this is helpful for integration with Windows Task Scheduler because you won't have to worry about Task Scheduler spinning up a huge number of these scripts at once.

If the python script is run using the `scheduled_lock_runner_batch.bat` runner, a command prompt window will be open while the script is running. This can be avoided by using the `scheduled_lock_runner_script.vbs` runner instead, which will hide the command prompt window.

# Dependencies

- psutil
