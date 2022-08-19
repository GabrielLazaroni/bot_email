from time import sleep
import pyautogui

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
sleep(0.5)
pyautogui.press('enter')
sleep(1)
pyautogui.write('outlook.com')
pyautogui.press('enter')
sleep(7)
pyautogui.click(x=1750, y=235)
sleep(1)

for i in range(0,20):
    pyautogui.click(x=2516, y=360)
    

