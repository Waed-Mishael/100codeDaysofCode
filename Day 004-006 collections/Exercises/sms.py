import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(msg: str, phone_number: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=msg,
            tab_close=True
        )
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    hi = "Hi "
    name = "Waad "
    msg1 = "Can you please Go to"
    places = ["kitchen", "Bathroom", "outside"]

    for j in range(2):  # This would be how many loop can we do in one day
        for i in range(2):  # This number should be the number of people we want to send messages to them.
            place = places[i]
            send_whatsapp_message(msg= hi + name + msg1 + " " + place, phone_number="+972587999213")  # we should make a thing
            # to get data from it, in our case the message should have the name of the person and a bit of
            # fixed text and a place from a list of the places or פעילות.

            # For that to be done I should think about an algorithm to do so.
            time.sleep(1)  # This it how much time we wait to the next message.
        time.sleep(4)  # This would be the time that we need to wait. let's say 45 min it should be 60*45







