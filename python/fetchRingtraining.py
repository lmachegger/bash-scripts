import requests
import time
from datetime import datetime

sleep_time = 90
counter = 0

while True:
    response = requests.get(
        'https://ringtraining.de/events')

    eventsOnline = False
    findStrings = ['brno', 'Brno', 'Most', 'most', 'rijeka', 'Rijeka']

    for findString in findStrings:
        if findString in response.text:
            eventsOnline = True
            break

    if eventsOnline:
        print('-----------------------------')
        print('EVENTS ARE ONLINE')
        print('-----------------------------')
        sleep_time = 360
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sleep_time = 90
        print('No Events!   checkNr: ' +
              str(counter) + '   time: ' + current_time)

    counter = counter+1
    time.sleep(sleep_time)
