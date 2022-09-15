import datetime
from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    plus_100 = timedelta(100)
    after_100dayes = start_100days + plus_100
    after_100dayes_str = "{:%Y-%m-%d}"
    return after_100dayes_str.format(after_100dayes)

def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return (pycon_date - pybites_founded).days
