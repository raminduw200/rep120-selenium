import schedule
import time
from scheduler_ import schedule_timetable


if __name__ == '__main__':
    schedule_timetable()
    while True:
        schedule.run_pending()
        if not schedule.jobs:
            break
        time.sleep(1)
