import pyautogui as pg
import time

time.sleep(5)

for i in range(100):
    pg.write(" eu te amo ")
    time.sleep(0.5)
    pg.press("Enter")
    