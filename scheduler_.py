import pandas as pd
import time
import datetime
import schedule

from rep120 import rep120_selenium as rep120

df = pd.read_csv('time-table.csv')
week_no = datetime.datetime.now().weekday()

day_courses = df[[df.columns[0], df.columns[week_no]]].copy()
today = day_courses.columns[1]
day_courses = day_courses.dropna(subset=['-', today])


def schedule_timetable():
    if week_no == 0:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().monday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 1:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().tuesday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 2:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().wednesday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 3:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().thursday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 4:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().friday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 5:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().saturday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
    elif week_no == 6:
        for time_, subj_ in zip(day_courses['-'], day_courses[today]):
            schedule.every().sunday.at(time_).do(rep120, str(int(subj_)))
            print(f"{time_} : {subj_} : {type(subj_)}")
