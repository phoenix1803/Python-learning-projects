#this uses pyautogui to spam text from a file and closes after finishing

import pyautogui, time
time.sleep(5)
f = open("abc.txt", 'r')
for a in f:
	pyautogui.typewrite(a)
	pyautogui.press("enter")
	time.sleep(1)
f.close()