import pynput
import time

from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

mouse = Controller()

'''
while key != Key.space:
    def on_press(key):
'''
# 3616 ->  5
# 5083 -> 10

i = 1

# 1430 aproximadamente 1 min
while i <= 1000:
    print(i)
    time.sleep(0.005)
    mouse.click(Button.left, 5)
    i += 1
    
'''
time.sleep(1)
mouse.click(Button.left, 1)
time.sleep(1)
mouse.click(Button.left, 1)
'''
