import random
import time
import pyautogui
import keyboard



# Initialize global variables
hotkey = '0'
user_x = 400
user_y = 125
counter = 0
pyautogui.FAILSAFE = False


# Define the input string for user options
input_str = """1. Change hotkey
2. Change mouse xy
3. Start farming points"""


# Ask the user what they want to do and store their choice in user_WTD variable
user_WTD = input('What do you want to do? Type the number.\n' + input_str + '\n')


# Check user input and perform actions based on the choice
if user_WTD == '1':  
    hotkey = input('Type the key you want to change it to. ')
    running = True

elif user_WTD == '2':
    user_x = int(input('Type the x coordinate: '))
    user_y = int(input('Type the y coordinate: '))
    
elif user_WTD == '3':
    
    running = True

else:
    print('Invalid input. Program will exit.')
    time.sleep(2.5)
    exit()


# warn user 
if user_x + user_y == 0:
  print('Failsafe is disabled. continuing is not recommend. Exit in 10 seconds if you want to stop.')
  time.sleep(10)
  running = True


list1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'k', 'l', 'n', 'z', 'x', 'c', 'v', 'b', 'n', 'm']


# Define the function to stop the loop when the hotkey is pressed
def stop_loop():
    global running
    running = False
    exit()


# Add the hotkey to stop the loop
keyboard.add_hotkey(hotkey, stop_loop)

running = True

# Start the loop when running = True
while running:
    
    # Starts timer
    start_time= time.time()

    # Click on the specified coordinates
    pyautogui.click(user_x, user_y)

    # Type 5 random letters
    for i in range(5):
        rk = random.choice(list1)
        keyboard.press(rk)

    # Presses Enter
    keyboard.press('enter')

    # Wait for 1.5 seconds for the page to load
    time.sleep(1.5)

    # Click on the specified coordinates again
    pyautogui.click(user_x, user_y)

    # Press Backspace 5 times to clear the text
    for i in range(5):
        keyboard.press('backspace')

    # adds 1 to counter
    counter += 1
    
    # Ends timer
    end_time= time.time() - start_time

    # prints counter and duration
    print(counter)
    print(end_time)
    
print('Quitting program in 20 seconds')
time.sleep(20)
exit()
