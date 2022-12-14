from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    line_lst = line.split(" ")
    if line_lst[1][0].isnumeric():
        extracted_timedate = datetime.fromisoformat(line_lst[1])
        return extracted_timedate


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    lst_shutdown_events = []

    for line in loglines:
        if isinstance(line, str) and len(line) > 1:
            line_splited = line.split()
            line_splited[-1] = line_splited[-1].replace('.', '')
            joined = line_splited[-2] + ' ' + line_splited[-1]
            if joined == SHUTDOWN_EVENT:
                lst_shutdown_events.append(line)

    min_datetime = convert_to_datetime(lst_shutdown_events[0])
    max_datetime = convert_to_datetime(lst_shutdown_events[-1])
    time_diffrence =max_datetime - min_datetime
    return time_diffrence