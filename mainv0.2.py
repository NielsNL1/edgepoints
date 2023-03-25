import random
import time
import pyautogui
import keyboard

list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'k', 'l', 'n', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

time.sleep(5)

def stop_loop():
    global running
    running = False



keyboard.add_hotkey('0', stop_loop)

running = True

while running:
    pyautogui.click(400,125)

    for i in range(5):
        rk = random.choice(list1)
        keyboard.press(rk)

    keyboard.press('enter')

    time.sleep(1.5)

    pyautogui.click(400,175)

    for i in range(5):
        keyboard.press('backspace')
