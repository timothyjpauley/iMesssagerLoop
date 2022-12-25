###messageb app
import time
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller

os.system("open -a Messages")

time.sleep(5)

for i in range(15):
    keyboard = Controller()
    keyboard.type("Merry Chistmas")
    keyboard.press(Key.enter)
    time.sleep(2)
