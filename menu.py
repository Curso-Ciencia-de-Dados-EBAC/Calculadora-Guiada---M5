import sys
import cursor
import pynput.keyboard as keyboard
from pynput.keyboard import Key

def select_option(key, i: int, options: list):
    l = len(options)
    
    if key == Key.up:
        i = i - 1 if i > 0 else l - 1
    if key == Key.down:
        i = i + 1 if i < l - 1 else 0
        
    for _ in range(l):
        ansi_cmd = f"\033[A\033[2K\033[1G"
        sys.stdout.write(ansi_cmd)
        
    for j, opt in enumerate(options):
        print(opt if j != i else f"> {opt}")
        
    return i
        
def menu(options: list):
    cursor.hide()
    
    # Initialize menu
    print("> " + options[0])
    for opt in options[1:]:
        print(opt)
        
    i = 0
    kill = False
    def callback(key):
        nonlocal i
        nonlocal kill
        i = select_option(key, i, options)
        
        if key == Key.enter or key == Key.esc:
            if key == Key.esc: kill = True
            return False
    
    with keyboard.Listener(on_press=callback, suppress=True) as listener:
        listener.join() 

    if kill: exit()
    cursor.show()
    return options[i]