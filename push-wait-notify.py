# THIS SCRIPT IS USED TO SYNCHRONIZE THE DATA FROM MY MAIN SERVER TO MY BACKUP SERVER WITH A DELAY SET BY THE USER AND SENDS NOTIFICATIONS WHEN IT'S STARTING / DONE
import os
import shutil
import requests
import time
import pushover

source = "M:/"
destination = "Z:/"
start = "Started backing up the NAS!"
done = "The NAS got successfully backed up!"
TOKEN = 'TOKEN'
USER_KEY = 'KEY'

def copy_files(src, dst):
    try:
        shutil.copy2(src, dst)
    except PermissionError:
        message = f"Skipping {src} due to a permission error."
        requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': message,
        })
        pass
    except Exception as e:
        message = f"Skipping {src} due to following error: {e}"
        requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': message,
        })

def start():
    requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': start,
        })
    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(destination, os.path.relpath(src_path, source))
            copy_files(src_path, dst_path)

delay = 60*60*input(int("Delay in hours between the backups? Enter number, then press enter to start! "))
while True:
    start()
    print("Successfully backed up your files from your NAS to the MyCloud!")
    requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': done,
        })
    time.sleep(delay)
    
