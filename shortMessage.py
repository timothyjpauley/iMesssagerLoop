###messageb app
import time
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller

os.system("open -a Messages")

time.sleep(5)

for i in range(5):
    keyboard = Controller()
    keyboard.type("Question: Who will win World Cup")
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type("Tim")
    time.sleep(5)