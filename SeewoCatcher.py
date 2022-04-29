from pynput import keyboard
import os as o
save = []       
debug = False    
def on_release(key):
    global save,debug
    print('{0} released'.format(
        key))
    if not debug:
        if key == keyboard.Key.tab:
            save.append("0")
        elif key == keyboard.Key.up:
            save.append("1")
        elif key == keyboard.Key.down:
            save.append("2")
        elif key == keyboard.Key.media_volume_up:
            save.append("3")
        elif key == keyboard.Key.media_volume_down:
            save.append("4")
            
        temp = "".join(save)
        if "000" in temp:
            debug = True
            save = []
            print("Debug!")  
    else:
        if key == keyboard.Key.tab:
            print("SeewoCatcher")
            #SeewoCatcher
        elif key == keyboard.Key.up:
            print("start Seewo")
            #start Seewo
        elif key == keyboard.Key.down:
            debug = False
            save = []
            print("End debug!")
        elif key == keyboard.Key.media_volume_up:
            print("cancel shutdown")
            #cancel shutdown
        elif key == keyboard.Key.media_volume_down:
            print("shutdown")
        #shutdown
        
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()