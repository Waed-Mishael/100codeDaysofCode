import copy
import queue
import datetime
import random

q_exhibits = queue.Queue()

NAME = 0
NUMBER = 1
ACTIVITY = 2
ACTIVITY_TIME = 3
EXHIBIT = 4
EXHIBIT_TIME = 5
CALL = 6
EXHIBIT_DURATION = 7

NUMBER_MADRICHIM_TODAY = 14


SHIFT_STARTS = "10:00"
SHIFT_ENDS = "16:00"

start_shift_time_object = datetime.datetime.strptime(SHIFT_STARTS, "%H:%M")
print(start_shift_time_object)
current_time = start_shift_time_object
end_shift_time_object = datetime.datetime.strptime(SHIFT_ENDS, "%H:%M")

ALL_EXHIBITS = ["modeain", "bniah", "merbaa", "yomholadet", "mistovv aleph", "mistovv biet", "komah 3", "khashmal gasher aver",
                "captcha", "ashlayot", "matmatica", "manof la giloy", "bniah2", "komah 3 2", "komah 3 3", "gasher aver", "yomholadet"]

without_madrich = []

TODAY_ALL_EXHIBITS = ALL_EXHIBITS[0:NUMBER_MADRICHIM_TODAY]

#function to insert madrichim and numbers and activity
TODAYS_MADRICHIM = ["None"]*NUMBER_MADRICHIM_TODAY

for i in range(len(TODAYS_MADRICHIM)):  # True means call him/her
    TODAYS_MADRICHIM[i] = ["name" + str(i), "number", "activity", "00:00", TODAY_ALL_EXHIBITS[i], datetime.datetime.strptime(SHIFT_STARTS, "%H:%M"), 40,True,[],[] ]
# TODAYS_MADRICHIM[0] = ["Waad", "+972587999213", "aish", "14:30", "modeain", datetime.datetime.strptime("14:00", "%H:%M") ,0, False]
# TODAYS_MADRICHIM[3] = ["Mona", "+972587999213", "panace", "13:00", "yomholadet", datetime.datetime.strptime("12:50", "%H:%M") ,0, False]
print(TODAYS_MADRICHIM)

START_BREAKS = datetime.datetime.strptime("12:10", "%H:%M")
duration = 10 * NUMBER_MADRICHIM_TODAY
END_BREAKS = START_BREAKS + datetime.timedelta(minutes=duration)


def add_10mins_to_each_one():
    for madrich in TODAYS_MADRICHIM:
        madrich[EXHIBIT_TIME] = madrich[EXHIBIT_TIME] + datetime.timedelta(minutes=10)
        print(madrich[5])



def find_available(without_madrich):
    choose_from = []
    for element in TODAY_ALL_EXHIBITS[4:]:
        if element not in without_madrich:
            choose_from.append(element)
    low_exhibit = random.choice(choose_from)
    for madrich in TODAYS_MADRICHIM:
        if madrich[EXHIBIT] == low_exhibit:
            return (madrich, low_exhibit)


def has_activity():
    all_has_acrivity = []
    for i in range(NUMBER_MADRICHIM_TODAY):  # check all madrichim, who has an activity?
        if TODAYS_MADRICHIM[i][ACTIVITY] != "activity":
            activity_madrich = TODAYS_MADRICHIM[i]  # all data about madrich
            all_has_acrivity.append(activity_madrich)
    return all_has_acrivity



def exchange(madrich_available, madrich_activity, current):
    """Change the available madrich place and start time"""
    madrich_available[4] = madrich_activity[4]
    madrich_available[5] = current.strftime("%H:%M")
    madrich_available[6] = True

    """Change the activity madrich to the activity"""
    madrich_activity[4] = madrich_activity[2]
    madrich_activity[5] = current.strftime("%H:%M")
    madrich_activity[6] = True
    return (madrich_available, madrich_activity)


def send_mahlef_high(lst, current, free_places_lst):
    for madrich in lst:
        madrich_time_object = datetime.datetime.strptime(madrich[3], "%H:%M") # 00:00
        if madrich_time_object == current + datetime.timedelta(minutes=20):
            if madrich[4] in ALL_EXHIBITS[0:3]:
                found = find_available(free_places_lst)
                if found[0] != madrich:
                    mahlef = found[0]
                    free_places_lst.append(found[1])
                    return exchange(mahlef, madrich, current)


def send_mahlef_low(lst, current, free_places_lst):
    for madrich in lst:
        madrich_time_object = datetime.datetime.strptime(madrich[3], "%H:%M") # 00:00
        if madrich_time_object == current + datetime.timedelta(minutes=10):
            if madrich[4] in ALL_EXHIBITS[4:]:
                found = find_available(free_places_lst)
                if found[0] != madrich:
                    mahlef = found[0]
                    free_places_lst.append(found[1])
                    return exchange(mahlef, madrich, current)


try_time = datetime.datetime.strptime("14:10", "%H:%M")

while current_time < end_shift_time_object:  # every 10 min check if there is a madrich that should go to activity
    # we can find an available madrich and send him to the actictivity madrich and then the last one to the activity
    #print(TODAYS_MADRICHIM)
    send_mahlef_high(has_activity(), current_time, without_madrich)
    send_mahlef_low(has_activity(), current_time, without_madrich)
    current_time = current_time + datetime.timedelta(minutes=10)



took_hafsaka = []

def give_hafsaka(took_hafsaka):
    pass

#         if activity_madrich_time_object == current_time + datetime.timedelta(minutes=10):
#             """when the madrich is at a low demanding place"""
#             if TODAYS_MADRICHIM[i][4] in ALL_EXHIBITS[4:]:
#                 # print(str(current_time) + " " + str(activity_madrich[0]) + " should go to " + str(activity_madrich[2]))
#                 TODAYS_MADRICHIM[i][4] = TODAYS_MADRICHIM[i][2]
#                 TODAYS_MADRICHIM[i][5] = current_time.strftime("%H:%M")
#                 TODAYS_MADRICHIM[i][6] = True
#                 shovats.append(TODAYS_MADRICHIM[i])
#         # fi khataa hoon

#         if START_BREAKS <= current_time <= END_BREAKS:
#             if TODAYS_MADRICHIM[i][0] not in took_hafsaka: # and TODAYS_MADRICHIM[i] not in shovats:
#                 if len(took_hafsaka) < number_madrichim_took+1:
#                     took_hafsaka.append(TODAYS_MADRICHIM[i][0])
#                     TODAYS_MADRICHIM[i][4] = "hafsaka"
#                     TODAYS_MADRICHIM[i][5] = current_time.strftime("%H:%M")
#                     TODAYS_MADRICHIM[i][6] = True
#                     shovats.append(TODAYS_MADRICHIM[i])
#     # print(shovats)


# def change_all_madrichim():
#     lst_1 = ["merbaa", "bnieh", "hafsaka"]
#     lst_without_mer_bneiah = []
#     for e in TODAY_ALL_EXHIBITS:
#         if e not in lst_1:
#             lst_without_mer_bneiah.append(e)
#     choose_from = copy.deepcopy(TODAY_ALL_EXHIBITS)
#     for madrich in TODAYS_MADRICHIM:
#         if madrich[4] not in lst_1:
#             new_position = random.choice(lst_without_mer_bneiah)
#             madrich[4] = new_position
#             choose_from.remove(new_position)
#         else:
#             new_position = random.choice(choose_from)
#             choose_from.remove(new_position)
    # for madrich in TODAYS_MADRICHIM:
    #     if madrich[4] == "bnieh" or "merbaa":
    #         new_position = random.choice(lst_without_mer_bneiah)
    #         done_for_this_round.append(new_position)


#     shovats = []
#     number_madrichim_took = len(took_hafsaka)
#     all_madrich_has_activity = has_activity()
#
#     for i in range(NUMBER_MADRICHIM_TODAY):  # check all madrichim who have an activities
#         activity_madrich = TODAYS_MADRICHIM[i]  # all data about madrich
#         activity_madrich_time_object = datetime.datetime.strptime(activity_madrich[3], "%H:%M") # 00:00
#
#         if activity_madrich_time_object == current_time + datetime.timedelta(minutes=20):
#             """when the madrich is at a high demanding place"""
#             if TODAYS_MADRICHIM[i][4] in ALL_EXHIBITS[0:3]:
#                 #hay bedha tasleh
#                 find_availabile_madrich = random.choice(TODAYS_MADRICHIM[4:])
#                 # print(str(current_time) + " " + "You Should send " + str(find_availabile_madrich[0]) + " to " + str(activity_madrich[4]))
#                 """Change the available madrich place and start time"""
#                 find_availabile_madrich[4] = TODAYS_MADRICHIM[i][4]
#                 find_availabile_madrich[5] = current_time.strftime("%H:%M")
#                 find_availabile_madrich[6] = True
#                 shovats.append(find_availabile_madrich)
#
#                 """Change the activity madrich to the activity"""
#                 TODAYS_MADRICHIM[i][4] = TODAYS_MADRICHIM[i][2]
#                 TODAYS_MADRICHIM[i][5] = current_time.strftime("%H:%M")
#                 TODAYS_MADRICHIM[i][6] = True
#                 shovats.append(TODAYS_MADRICHIM[i])

#change_all_madrichim()