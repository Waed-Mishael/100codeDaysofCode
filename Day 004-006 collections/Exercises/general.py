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
SET = 8
LST_CANT = 9

ALL_EXHIBITS = ["modeain", "bniah", "merbaa", "yomholadet", "mistovv aleph", "mistovv biet", "komah 3 ",
                "khashmal gasher aver", "captcha", "ashlayot", "matmatica", "manof la giloy", "bniah2", "komah 3 2 ",
                "komah 3 3", "gasher aver", "yomholadet"]

TODAY_ALL_EXHIBITS = ALL_EXHIBITS[0:NUMBER_MADRICHIM_TODAY]
ALL_EXHIBITS_NOW = copy.deepcopy(TODAY_ALL_EXHIBITS)
# function to insert madrichim and numbers and activity
# TODAYS_MADRICHIM = ["None"] * NUMBER_MADRICHIM_TODAY
TODAYS_MADRICHIM = [['name0', 'number', 'activity', '00:00', 'bnieh', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name1', 'number', 'activity', '00:00', 'bniah', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name2', 'number', 'activity', '00:00', 'merbaa', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name3', 'number', 'activity', '00:00', 'yomholadet', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name4', 'number', 'activity', '00:00', 'mistovv aleph', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name5', 'number', 'activity', '00:00', 'mistovv biet', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name6', 'number', 'activity', '00:00', 'komah 3', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name7', 'number', 'activity', '00:00', 'khashmal gasher aver', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name8', 'number', 'activity', '00:00', 'captcha', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name9', 'number', 'activity', '00:00', 'ashlayot', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name10', 'number', 'activity', '00:00', 'matmatica', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name11', 'number', 'activity', '00:00', 'manof la giloy', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name12', 'number', 'activity', '00:00', 'bniah2', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []], ['name13', 'number', 'activity', '00:00', 'komah 3 2', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []]]

START_BREAKS = datetime.datetime.strptime("12:10", "%H:%M")
duration = 10 * NUMBER_MADRICHIM_TODAY
END_BREAKS = START_BREAKS + datetime.timedelta(minutes=duration)

NUMBER_MADRICHIM_ACTIVITY = 2
number_of_madrichim_now = NUMBER_MADRICHIM_TODAY - NUMBER_MADRICHIM_ACTIVITY
CHANG_ALL_NOW = copy.deepcopy(TODAYS_MADRICHIM[:number_of_madrichim_now])  # this items from lst should removed from it

def change_all():
    """we can change the place of all the madrichim but if there is a duplication of a place we could send the
    madrich to the same place!
     it might be a good idea to use the exchange function of this madrich with an other madrich
     """
    lshovats = copy.deepcopy(TODAY_ALL_EXHIBITS)
    for madrich in TODAYS_MADRICHIM:
        if madrich[EXHIBIT_DURATION] < 40:  # if madrich is not there too long remove his place from the changing
            lshovats.remove(madrich[EXHIBIT])

        else:
            exhibit_before = madrich[EXHIBIT]  # remove his current place
            if exhibit_before in lshovats:
                lshovats.remove(exhibit_before)  # remove it from the choices
                madrich[EXHIBIT] = random.choice(lshovats)  # choose a new place for him
                lshovats.remove(madrich[EXHIBIT])  # remove the choice from the list
                lshovats.append(exhibit_before)  # add his place so another madrich can go ther
            else:
                madrich[EXHIBIT] = random.choice(lshovats)  # choose a new place for him where we cant choose his
                # last place
                lshovats.remove(madrich[EXHIBIT])  # remove the choice from the list

            madrich[EXHIBIT_DURATION] = 0
        print(madrich[EXHIBIT])
##################################################################
ALL_EXHIBITS_NOW = ["bniah", "modeain", "merba"]

def was_there(madrich):
    if madrich[SET] == len(TODAY_ALL_EXHIBITS):
        madrich[SET] = []                       # if he/she was in all posible places reset the set

    """This function removes all the exhibits that the madrich was at"""
    for item in ALL_EXHIBITS_NOW:
        if item in madrich[SET]:
            ALL_EXHIBITS_NOW.remove(item)


def if_was_at(madrich, exhibit):
    """this function checks if the madrich was at a spacific exhibit"""
    for item in madrich[SET]:
        if item == exhibit:
            return True
    return False


def exchange_activity(madrich_available, madrich_activity, current):
    """Change the available madrich place and start time with an activity madrich"""
    madrich_available[EXHIBIT] = madrich_activity[EXHIBIT]
    madrich_available[EXHIBIT_TIME] = current.strftime("%H:%M")
    madrich_available[CALL] = True

    """Change the activity madrich to the activity"""
    madrich_activity[EXHIBIT] = madrich_activity[ACTIVITY]
    madrich_activity[EXHIBIT_TIME] = current.strftime("%H:%M")
    madrich_activity[CALL] = True
    return (madrich_available, madrich_activity)


def exchange(madrich_available, madrich ):
    """exchange 2 madrichim with each other"""
    # I should add the time for both of them
    madrich_available_exhib = madrich_available[EXHIBIT]
    madrich_available[EXHIBIT] = madrich[EXHIBIT]
    madrich_available[EXHIBIT_DURATION] = 0
    madrich_available[EXHIBIT_TIME] = madrich_available[EXHIBIT_TIME]
    madrich_available[CALL] = True

    """Change the activity madrich to the activity"""
    madrich[EXHIBIT] = madrich_available_exhib
    madrich[EXHIBIT_TIME] = madrich[EXHIBIT_TIME]
    madrich[EXHIBIT_DURATION] = 0
    madrich[CALL] = True
    return (madrich_available, madrich)
############################################################################

def dont_send_to(lst, madrich):   # ["merba" , "bnieh"] or ["komah 3" , "komah 3 2" , "komah 3 3"] and madrich_exhibit = madrich[EXHIBIT]
    """finds the places that the madrich cant go to"""
    was_there(madrich)
    deleted = []
    print(madrich[EXHIBIT])

    if madrich[EXHIBIT] in ALL_EXHIBITS_NOW:
        ALL_EXHIBITS_NOW.remove(madrich[EXHIBIT])
    if madrich[EXHIBIT] in lst:  # if the madrich is at a place that could have duplications
        ALL_EXHIBITS_NOW.remove(madrich[EXHIBIT])
        print("hi")
        for item in lst:                                # loop on these dupls and remove them
            if item in ALL_EXHIBITS_NOW:                # if they were at our current changing list
                ALL_EXHIBITS_NOW.remove(item)
                deleted.append(item)
        if len(ALL_EXHIBITS_NOW)>0:           # if we still have somthing to choose from
            madrich[SET].append(madrich[EXHIBIT])
            exhibit = random.choice(ALL_EXHIBITS_NOW)
            madrich[EXHIBIT] = exhibit
            madrich[EXHIBIT_DURATION] = 0

        else:
            for other_madrich in TODAYS_MADRICHIM:
                # if has activity
                # if at hafsaka
                print("1")
                if other_madrich != madrich:
                    for ex in lst:
                        print(deleted)
                        print(exchange(other_madrich, madrich))
                        return

                # I think it should exchange with an other madrich
    for item in deleted:
        ALL_EXHIBITS_NOW.append(item)


print(dont_send_to(['merba','bniah'],['name0', 'number', 'activity', '00:00', 'bnieh', datetime.datetime(1900, 1, 1, 10, 0), 40, True, [], []]))