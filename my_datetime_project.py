"""This would be a Game, very similar to one of the exhibits in an
exhibition called "Time to Move" that was in the Science Museum in
 Jerusalem """
import datetime


def exit_any_time(messege):
    """This function returns True if the input is 'exit' else it returns False"""
    if messege == "exit" or "Exit" or "EXIT":
        return True
    else:
        return False


the_input = input("You are required to expect how long the minute will be.\npress s to start\n"
                  "then press e when you think the minute ended \nto end the game type exit\n")


def check_if_alpha(an_input):
    """This function checks if the input is a letter or a word"""
    if an_input.isalpha():
        return True
    return False


def start_game():
    """check when the player guesses the minute."""
    start = datetime.datetime.now()
    input_after_start = input("The game started don't forget to press 'e' when you think the minute ended or 'exit' to exit\n")
    exit_any_time(input_after_start)
    while True:
        if input_after_start.isalpha() and input_after_start == 'e':  # the inout is e
            end = datetime.datetime.now()
            period = end - start
            print("the time that you thought is a minute is: " + str(period))
            if int(period.total_seconds()) == 60:
                print("Perfect! You did it!")
            elif int(period.total_seconds()) < 60:
                print("Opps! A minute is longer than that!")
            else:
                print("Opps! You waited to much!")
            break
        elif input_after_start.isalpha() and input_after_start == 'exit':  # the input is not e But it is exit
            exit_any_time(input_after_start)
        else:
            input_after_start = input("This is not 'e'. Press 'e' to end! or type 'exit' to exit\n")


while True:
    """check if the player want to play or want to end the game"""
    if not check_if_alpha(the_input):
        the_input = input("Be careful! insert just letters\npress 's' or type 'exit'\n")
    elif the_input != 's' and the_input != "exit":
        the_input = input("Please insert 's' to start or 'exit' to exit the game\n")
    elif the_input == 's':
        start_game()
        break
    elif the_input == "exit":
        if exit_any_time(the_input):
            break
