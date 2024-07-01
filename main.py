import keyboard
import time
import pyautogui as pyg
from PIL import Image
from img_analyzer import *
pyg.FAILSAFE = False


pos_list = [pos]
def claim(pos_list):
    for el in pos_list:
        pyg.click(el)


sx = 0
sy = 0
pos_list = []
on = True

print("On")
while on:
    if keyboard.is_pressed('q'):
        on = False
        break
    pyg.hotkey('ctrl', 'r')
    time.sleep(1)
    claim(pos_list)
