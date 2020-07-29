from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()

def on_release(key):
    try:
        count = 0
        while (count < 9):
            kb.type(u'Hello')
            kb.press(Key.enter)
            kb.release(Key.enter)

    except:
        pass

while True:
    with keyboard.Listener(
        on_release = on_release) as listener:
        listener.join()
