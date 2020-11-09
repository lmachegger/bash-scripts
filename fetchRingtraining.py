import requests
import time

counter = 0

while True:
    print("Check: " + str(counter))
    response = requests.get(
        'https://ringtraining.de/events')

    findString = 'Es sind keine Event geplant'

    if findString in response.text:
        print('No Events')
    else:
        print('-----------------------------')
        print('EVENTS ARE ONLINE')
        print('-----------------------------')

    print('-----------------------')

    counter = counter+1
    time.sleep(90)
