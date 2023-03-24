import keyboard
import random
import time
import pyautogui


list1 = [ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'k','l', 'n', 'z', 'x', 'c', 'v', 'b', 'n' ,'m' ]

time.sleep(5)

while True:

    rk = random.choice(list1)
    keyboard.press(rk)

    rk = random.choice(list1)
    keyboard.press(rk)

    rk = random.choice(list1)
    keyboard.press(rk)

    rk = random.choice(list1)
    keyboard.press(rk)

    rk = random.choice(list1)
    keyboard.press(rk)

    keyboard.press('enter')

    time.sleep(3)

    pyautogui.click(500,130)
    
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')
    keyboard.press('backspace')
