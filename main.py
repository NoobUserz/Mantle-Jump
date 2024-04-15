import time
import keyboard
import win32api
import pyautogui
def jump_off_zipline():
    print("Jumping off zipline...")
    # Press jump key
    keyboard.press('space')
    keyboard.release('space')
    time.sleep(0.4)

def hold_crouch_forward():
    print("forward...")
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')
    time.sleep(0.3)

def tap_backwards_flick_down():
    print("Tapping backwards + flicking down...")
    # Flick mouse downwards (simulation)
    win32api.mouse_event(0x01, 0, 999999)
    time.sleep(0.1)
    keyboard.press('s')
    time.sleep(0.09)
    keyboard.release('s')
    time.sleep(0.035)
    # Tap backwards key


def super_jump():
    print("Performing super jump...")
    # Press interact key
    keyboard.press('e')
    time.sleep(0.035)
    keyboard.release('e')
    scroll_amount = 99999 # Increase the amount of scroll for faster scrolling
    for _ in range(5):  # Repeat scrolling 5 times for smoother effect
        pyautogui.scroll(scroll_amount, x=100, y=100)
        time.sleep(0.000000001)

def start_execution(event):
    if event.name == 'x':
        print("Starting execution...")
        jump_off_zipline()
        hold_crouch_forward()
        tap_backwards_flick_down()
        super_jump()
        print("Actions executed successfully.")

if __name__ == "__main__":
    print("Press 'x' to start actions...")
    keyboard.on_press(start_execution)
    keyboard.wait('-')  # Wait for '-' key to exit
