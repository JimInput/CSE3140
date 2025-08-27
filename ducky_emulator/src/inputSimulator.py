from sys import platform
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

keys = {
        "DELETE" : Key.delete,
        "SHIFT" : Key.shift,
        "CONTROL" : Key.ctrl,
        "CTRL" : Key.ctrl,
        "ENTER" : Key.enter,
        "HOME" : Key.home,
        "PAGEUP" : Key.page_up,
        "PAGEDOWN" : Key.page_down,
        "WINDOWS" : Key.cmd,
        "GUI" : Key.cmd,
        "UPARROW" : Key.up,
        "UP" : Key.up,
        "LEFTARROW" : Key.left,
        "LEFT" : Key.left,
        "RIGHTARROW" : Key.right,
        "RIGHT" : Key.right,
        "DOWNARROW" : Key.down,
        "BACKSPACE" : Key.backspace,
        "DOWN" : Key.down,
        "TAB" : Key.tab,
        "ESCAPE" : Key.esc,
        "ESC" : Key.esc,
        "ALT" : Key.alt,
        "END" : Key.end,
        "SPACE" : Key.space,
        "F1" : Key.f1,
        "F2" : Key.f2,
        "F3" : Key.f3,
        "F4" : Key.f4,
        "F5" : Key.f5,
        "F6" : Key.f6,
        "F7" : Key.f7,
        "F8" : Key.f8,
        "F9" : Key.f9,
        "F10" : Key.f10,
        "F11" : Key.f11,
        "F12" : Key.f12,
        "F13" : Key.f13}

if platform == "win32":
    keys.update({
        "INSERT" : Key.insert,
        "BREAK" : Key.pause,
        "PAUSE" : Key.pause,
        "APP" : Key.menu,
        "MENU" : Key.menu})

elif platform == "darwin":
    keys.update({
        "COMMAND" : Key.cmd})

def SimulateModifiedKeyStroke(modifierKey, key):
    modifierKey, key = Text2Keycode(modifierKey, key)
    keyboard.press(modifierKey)
    if key:
        keyboard.press(key)
        keyboard.release(key)
    keyboard.release(modifierKey)

def SimulateKeyPress(key):
    key = Text2Keycode(key.lower())[0]
    keyboard.press(key)
    keyboard.release(key)

def SimulateTextEntry(text:str, delay:float = 13/1000.0):
    keyboard.press(text[0])
    keyboard.release(text[0])
    for char in text[1:]:
        sleep(delay)
        keyboard.press(char)
        keyboard.release(char)
        

def Text2Keycode(*args):
    result = []
    for string in args:
        if string.upper() in keys:
            string = keys[string.upper()]
        result += [string]
    return result

# Testing
if __name__ == "__main__":
    var1, var2 = Text2Keycode("GUI", "r")
    print(var1, var2)

    SimulateModifiedKeyStroke("gui", "r")

    sleep(3)

    SimulateTextEntry("notepad.exe")

    sleep(0.1)

    SimulateKeyPress("enter")