import requests
import time
import pushover

#THIS SCRIPT IS USED TO MONITOR MY SERVER AND ALERT ME WHEN IT'S DOWN

# Pushover API credentials and user key
PUSHOVER_API_KEY = 'a43cbrkw1tpime3jzdwwutb97rpwpr'
PUSHOVER_USER_KEY = 'uccs42b9qhkvm312yxjb8m5fr7sh6x'

# URL of the server to check
URL = 'https://192.168.178.86'
UP = 'Hourly check: TrueNAS is up and running!'
TOKEN = 'TOKEN'
USER_KEY = 'KEY'

while True:
    try:
        # Check the server status code
        response = requests.get(URL, verify = False)
        response.raise_for_status()
        requests.post('https://api.pushover.net/1/messages.json', data={
            'token': TOKEN,
            'user': USER_KEY,
            'message': UP,
        })
        # Wait for 10 minutes before checking again
        time.sleep(600)
    except requests.exceptions.HTTPError as e:
        # Wait for SLEEP_TIME seconds before checking again
            DOWN = f"TrueNAS encountered an HTTP error: {e}"
            requests.post('https://api.pushover.net/1/messages.json', data={
                'token': TOKEN,
                'user': USER_KEY,
                'message': DOWN,
            })
            time.sleep(600)
    except requests.exceptions.RequestException as e:
            DOWN = f"TrueNAS is not accessible: {e}"
            requests.post('https://api.pushover.net/1/messages.json', data={
                'token': TOKEN,
                'user': USER_KEY,
                'message': DOWN,
            })
            time.sleep(600)