# THIS SCRIPT IS USED TO SYNCHRONIZE THE DATA FROM MY MAIN SERVER TO MY BACKUP SERVER WITH A DELAY SET BY THE USER

import os
import shutil

source = "M:/"
destination = "Z:/"

def copy_files(src, dst):
    try:
        shutil.copy2(src, dst)
    except PermissionError:
        print(f"Skipping {src} due to a permission error.")
        pass
    except Exception as e:
        print(f"Skipping {src} due to following error: {e}")
def start():
    for root, dirs, files in os.walk(source):
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(destination, os.path.relpath(src_path, source))
            copy_files(src_path, dst_path)

delay = 60*60*input(int("Delay in hours between the backups? Enter number, then press enter to start! "))
while True:
    start()
    print("Successfully backed up your files from your NAS to the MyCloud!")
    
