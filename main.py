import pyautogui
import keyboard
import random
import time
import threading

# Declaring constants
INTERRUPT_KEY = 'esc'
mouseMovementEnabled = True

def simulate_random_mouse_movement():
    screen_width,screen_height = pyautogui.size()
    while mouseMovementEnabled:
        x = random.randint(0,screen_width)
        y = random.randint(0,screen_height)
        pyautogui.moveTo(x,y,duration=1)
        for i in range(0,6000):
            if mouseMovementEnabled:
                time.sleep(.01)
        pyautogui.press('shift')

def listen_for_interrupt():
    global mouseMovementEnabled
    while True:
        if keyboard.is_pressed(INTERRUPT_KEY):
            # threading.Lock().release()
            mouseMovementEnabled = False
            break

if __name__ == "__main__":
    print(f"Press {INTERRUPT_KEY} to stop the program")
    thread = threading.Thread(target=simulate_random_mouse_movement)
    thread.start()
    thread1 = threading.Thread(target=listen_for_interrupt)
    thread1.start()
    thread1.join()
    
    thread.join()
    exit()
