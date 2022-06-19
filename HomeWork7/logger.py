

import datetime


def add_log(action):

    with open("logs.txt", "a+", encoding="utf-8") as data:
        dt = datetime.datetime.now()
        data.write(f"{dt} {action}\n")