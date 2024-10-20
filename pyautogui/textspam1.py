#this uses pyautogui and a text file to spam the text in the file
import pyautogui, time

while True:
    time.sleep(5)
    with open("abc.txt", 'r') as f:
        for a in f:
            pyautogui.typewrite(a)
            pyautogui.press("enter")
            time.sleep(1)
