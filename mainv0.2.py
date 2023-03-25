import random
import time
import pyautogui
import keyboard

list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'k', 'l', 'n', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

time.sleep(5)

def stop_loop():
    global running
    running = False


# Replace the zero with a other key if you want to change the hotkey.
keyboard.add_hotkey('0', stop_loop)

running = True

# This is so that you have time to open the browser, it is not nessacry and you can delelte this line of code if you want.
time.sleep(5)

while running:
    # You might need to change this depending on what browser you use. 400 = x 125 = y
    pyautogui.click(400,125)

    for i in range(5):
        rk = random.choice(list1)
        keyboard.press(rk)

    keyboard.press('enter')

    time.sleep(1.5)

    pyautogui.click(400,175)

    for i in range(5):
        keyboard.press('backspace')
