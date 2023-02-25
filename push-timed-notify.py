# THIS SCRIPT IS USED TO SYNCHRONIZE THE DATA FROM MY MAIN SERVER TO MY BACKUP SERVER EVERYDAY AT MIDNIGHT

import os
import shutil
import datetime
import pytz
import pushover
import requests

source = "M:/"
destination = "Z:/"
german_tz = pytz.timezone('Europe/Berlin')
current_time = datetime.datetime.now(tz=german_tz)
start = "Started backing up the NAS!"
done = "The NAS got successfully backed up!"
TOKEN = 'TOKEN'
USER_KEY = 'KEY'

def copy_files(src, dst):
    try:
        shutil.copy2(src, dst)
    except PermissionError:
        print(f"Skipping {src} due to a permission error.")
        pass

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

while True:
    if current_time.hour == 0 and current_time.minute == 0:
        start()
        print("Successfully backed up your files from your NAS to the MyCloud!")
        requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': done,
        })
