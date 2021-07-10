from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener

global MOUSE 
MOUSE = Controller()

# up = Pressed at (237, 316)
# do = Pressed at (237, 461)
# ri = Pressed at (306, 377)
# le = Pressed at (172, 377)
# 
# L = Pressed at (550, 674)
# R = Pressed at (815, 677)
# P = Pressed at (666, 673)
# 
# Y = Pressed at (1122, 310)
# A = Pressed at (1122, 463)
# B = Pressed at (1199, 380)
# X = Pressed at (1049, 380)
# 

def cust_click(x,y):
    MOUSE.position = (x,y)
    # MOUSE.click(Button.left)
    MOUSE.press(Button.left)

def up():
    cust_click(237, 316)

def down():
    cust_click(237, 461)

def right():
    cust_click(306, 377)

def left():
    cust_click(172, 377)

###########################

def pause():
    cust_click(666, 673)

def back():
    cust_click(815, 677)

def select():
    cust_click(550, 674)

###########################

def pres_y():
    cust_click(1122, 310)

def pres_a():
    cust_click(1122, 463)

def pres_b():
    cust_click(1199, 380)

def pres_x():
    cust_click(1049, 380)


def cek_key(key):
    try: k = key.char
    except: k = None
    return k

def on_press(key):
    k = cek_key(key)
    if k is not None: 
        if key.char == ('w'): pres_y()
        if key.char == ('a'): pres_x()
        if key.char == ('s'): pres_a()
        if key.char == ('d'): pres_b()
        if key.char == ('p'): pause()
    else:
        if key == Key.left:
            left()
        elif key == Key.right:
            right()
        elif key == Key.up:
            up()
        elif key == Key.down:
            down()
        elif key == Key.space:
            select()
        elif key == Key.backspace:
            backspace()

def on_release(key):
    if key == Key.esc:
        return False
    else:
        k = cek_key(key)
        if k is not None and k == ('w') or k == ('a') or k == ('s') or k == ('d') or k == ('p'):
            MOUSE.release(Button.left)
        elif key == Key.right or key == Key.left or key == Key.up or key == Key.down or key == Key.space or key == Key.backspace:
            MOUSE.release(Button.left)

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()