import pyautogui
import keyboard
import random
import asyncio

# Declaring constants
INTERRUPT_KEY = 'ctrl+shift+q'
movement_interval = 60  # Interval in seconds for mouse movement
polling_interval = 20

async def simulate_random_mouse_movement(stop_event):
    screen_width, screen_height = pyautogui.size()
    while not stop_event.is_set():
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        
        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.press('numlock')
        # print('Movement Triggered.')
        
        # We wait in small increments so we can react to the stop_event quickly
        try:
            await asyncio.wait_for(stop_event.wait(), timeout=polling_interval)
        except asyncio.TimeoutError:
            pass

def on_interrupt(stop_event):
    print(f"\nInterrupt detected ({INTERRUPT_KEY})! Shutting down...")
    stop_event.set()

# async def listen_for_interrupt(stop_event):
#     print(f"Press '{INTERRUPT_KEY}' to stop.")
#     while not stop_event.is_set():
#         # keyboard.is_pressed is blocking, but fast enough for this loop
#         if keyboard.is_pressed(INTERRUPT_KEY):
#             print("\nInterrupt detected! Shutting down...")
#             stop_event.set()
#             break
#         await asyncio.sleep(stop_event)

async def main():

    # Use an actual asyncio Event object
    stop_event = asyncio.Event()


    # EVENT-DRIVEN INTERRUPT: Uses almost zero CPU
    # This replaces the entire 'listen_for_interrupt' loop
    keyboard.add_hotkey(INTERRUPT_KEY, lambda:on_interrupt(stop_event))
    print(f"Press '{INTERRUPT_KEY}' to stop.")

    try:
        await simulate_random_mouse_movement(stop_event)
    finally:
        keyboard.remove_all_hotkeys()

    # Await gather so the script stays alive until both tasks finish
    # try:
    #     await asyncio.gather(
    #         listen_for_interrupt(stop_event),
    #         simulate_random_mouse_movement(stop_event)
    #     )
    # except Exception as e:
    #     print(f"An error occurred: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass # Handle Ctrl+C gracefully
