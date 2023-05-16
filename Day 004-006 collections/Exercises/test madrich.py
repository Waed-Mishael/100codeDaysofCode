import copy
import queue
import datetime
import random

q_exhibits = queue.Queue()

NUMBER_MADRICHIM_TODAY = 14
NAME = 0
NUMBER = 1
ACTIVITY = 2
ACTIVITY_TIME = 3
EXHIBIT = 4
EXHIBIT_TIME = 5
EXHIBIT_DURATION = 6
CALL = 7

ALL_EXHIBITS = ["modeain", "bniah", "merbaa", "yomholadet", "mistovv aleph", "mistovv biet", "komah 3 ",
                "khashmal gasher aver", "captcha", "ashlayot", "matmatica", "manof la giloy", "bniah2", "komah 3 2 ",
                "komah 3 3", "gasher aver", "yomholadet"]
TODAY_ALL_EXHIBITS = ALL_EXHIBITS[0:NUMBER_MADRICHIM_TODAY]

# function to insert madrichim and numbers and activity
TODAYS_MADRICHIM = ["None"] * NUMBER_MADRICHIM_TODAY
TODAYS_MADRICHIM = [['name0', 'number', 'activity', '00:00', 'modeain', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name1', 'number', 'activity', '00:00', 'bniah', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name2', 'number', 'activity', '00:00', 'merbaa', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name3', 'number', 'activity', '00:00', 'yomholadet', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name4', 'number', 'activity', '00:00', 'mistovv aleph', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name5', 'number', 'activity', '00:00', 'mistovv biet', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name6', 'number', 'activity', '00:00', 'komah 3', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name7', 'number', 'activity', '00:00', 'khashmal gasher aver', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name8', 'number', 'activity', '00:00', 'captcha', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name9', 'number', 'activity', '00:00', 'ashlayot', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name10', 'number', 'activity', '00:00', 'matmatica', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name11', 'number', 'activity', '00:00', 'manof la giloy', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name12', 'number', 'activity', '00:00', 'bniah2', datetime.datetime(1900, 1, 1, 10, 0), 40, True], ['name13', 'number', 'activity', '00:00', 'komah 3 2', datetime.datetime(1900, 1, 1, 10, 0), 40, True]]

START_BREAKS = datetime.datetime.strptime("12:10", "%H:%M")
duration = 10 * NUMBER_MADRICHIM_TODAY
END_BREAKS = START_BREAKS + datetime.timedelta(minutes=duration)

def find_who_is_there(exh2 ,exh):
    for mad in TODAYS_MADRICHIM:
        if mad[EXHIBIT] == exh:
            mad[EXHIBIT] = exh2


def change_all():
    lshovats = copy.deepcopy(TODAY_ALL_EXHIBITS)
    lshovats2 = copy.deepcopy(TODAY_ALL_EXHIBITS)  # without modein and merbaa
    if "merbaa" in lshovats2:
        lshovats2.remove("merbaa")
    if "bniah" in lshovats2:
        lshovats2.remove("bniah")

    lshovats3 = copy.deepcopy(TODAY_ALL_EXHIBITS)
    if "komah 3" in TODAY_ALL_EXHIBITS:
        lshovats3.remove("komah 3")
    if "komah 3 2" in TODAY_ALL_EXHIBITS:
        lshovats3.remove("komah 3 2")
    if "komah 3 3" in TODAY_ALL_EXHIBITS:
        lshovats3.remove("komah 3 3")
    if "bniah2" in lshovats2:
        lshovats2.remove("bniah2")
    for madrich in TODAYS_MADRICHIM:
        if madrich[EXHIBIT] == "merbaa" or madrich[EXHIBIT] == "bniah" or madrich[EXHIBIT] == "bniah2":
            if madrich[EXHIBIT_DURATION] < 40:
                lshovats.remove(madrich[EXHIBIT])
            madrich[EXHIBIT] = random.choice(lshovats2)
            if madrich[EXHIBIT] == "merbaa":
                find_who_is_there("merbaa", madrich[EXHIBIT])
            if madrich[EXHIBIT] == "bniah":
                find_who_is_there("bniah", madrich[EXHIBIT])
            if madrich[EXHIBIT] == "bniah2":
                find_who_is_there("bniah2", madrich[EXHIBIT])
            lshovats.remove(madrich[EXHIBIT])
            lshovats2.remove(madrich[EXHIBIT])
            madrich[EXHIBIT_DURATION] = 0


    for madrich in TODAYS_MADRICHIM:

        if madrich[EXHIBIT] == "komah3" or madrich[EXHIBIT] == "komah3 2" or madrich[EXHIBIT] == "komah3 3":
            print(madrich[EXHIBIT])

            if madrich[EXHIBIT_DURATION] < 40:
                lshovats.remove(madrich[EXHIBIT])
            madrich[EXHIBIT] = random.choice(lshovats2)
            if madrich[EXHIBIT] == "komah3":
                find_who_is_there("komah3", madrich[EXHIBIT])
            if madrich[EXHIBIT] == "komah3 2":
                find_who_is_there("komah3 2", madrich[EXHIBIT])
            if madrich[EXHIBIT] == "komah3 3":
                find_who_is_there("komah3 3", madrich[EXHIBIT])
            lshovats.remove(madrich[EXHIBIT])
            lshovats3.remove(madrich[EXHIBIT])
            madrich[EXHIBIT_DURATION] = 0
            print(madrich[EXHIBIT])



        else:
            print(madrich[EXHIBIT])
            if madrich[EXHIBIT_DURATION] < 40 and madrich[EXHIBIT] in lshovats:
                lshovats.remove(madrich[EXHIBIT])
            else:
                exhibit_before = madrich[EXHIBIT]
                if exhibit_before in lshovats:
                    lshovats.remove(exhibit_before)
                    madrich[EXHIBIT] = random.choice(lshovats)
                    lshovats.remove(madrich[EXHIBIT])
                    lshovats.append(exhibit_before)
                elif len(lshovats) > 0:
                    madrich[EXHIBIT] = random.choice(lshovats)
                    lshovats.remove(madrich[EXHIBIT])
                madrich[EXHIBIT_DURATION] = 0
            print(madrich[EXHIBIT])



change_all()