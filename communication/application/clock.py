import time
import datetime
import schedule

def clock() -> list:
    """Return a list containing year, month, day, minute"""
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    minute = now.minute
    return [year, month, day, minute]