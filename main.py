import keyboard
import time
import threading

is_running = False
def key_loop():
    global is_running
    while is_running:
        keyboard.press_and_release("w")#w
        keyboard.press_and_release("s")
        time.sleep(0.1)  # 0.1s

def start_loop():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=key_loop, daemon=True).start()

def stop_loop():
    global is_running
    is_running = False

keyboard.add_hotkey('f7', start_loop)
keyboard.add_hotkey('f8', stop_loop)
keyboard.wait('esc')

