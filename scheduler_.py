import pandas as pd
import datetime
import schedule
from tabulate import tabulate
from rep120 import rep120_selenium as rep120

df = pd.read_csv('time-table.csv')
# week_no = datetime.datetime.now().weekday()
output = []


def schedule_timetable():
    for week_day in range(5):
        day_courses = df[[df.columns[0], df.columns[week_day + 1]]].copy()
        day = day_courses.columns[1]
        day_courses = day_courses.dropna(subset=['-', day])

        if week_day == 0:
            for time_, subj_ in zip(day_courses['-'], day_courses[day]):
                schedule.every().monday.at(time_).do(rep120, str(int(subj_)))
                output.append(["Monday", time_, subj_, "Scheduled"])
        elif week_day == 1:
            for time_, subj_ in zip(day_courses['-'], day_courses[day]):
                schedule.every().tuesday.at(time_).do(rep120, str(int(subj_)))
                output.append(["Tuesday", time_, subj_, "Scheduled"])
        elif week_day == 2:
            for time_, subj_ in zip(day_courses['-'], day_courses[day]):
                schedule.every().wednesday.at(time_).do(rep120, str(int(subj_)))
                output.append(["Wednesday", time_, subj_, "Scheduled"])
        elif week_day == 3:
            for time_, subj_ in zip(day_courses['-'], day_courses[day]):
                schedule.every().thursday.at(time_).do(rep120, str(int(subj_)))
                output.append(["Thursday", time_, subj_, "Scheduled"])
        elif week_day == 4:
            for time_, subj_ in zip(day_courses['-'], day_courses[day]):
                schedule.every().friday.at(time_).do(rep120, str(int(subj_)))
                output.append(["Friday", time_, subj_, "Scheduled"])
        # elif week_day == 5:
        #     for time_, subj_ in zip(day_courses['-'], day_courses[day]):
        #         schedule.every().saturday.at(time_).do(rep120, str(int(subj_)))
        #         table.append(["Saturday", time_, subj_, "Scheduled"])
        # elif week_day == 6:
        #     for time_, subj_ in zip(day_courses['-'], day_courses[day]):
        #         schedule.every().sunday.at(time_).do(rep120, str(int(subj_)))
        #         table.append(["Sunday", time_, subj_, "Scheduled"])
    print(tabulate(output, headers=["Day", "Time", "Subject", "Schedule"]))
