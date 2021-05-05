from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import colorsys
import math
import time
import numpy
import itertools
import unicornhathd

print("""Welcome to the Real World
Do Not Disturb light.
Press Ctrl+C to exit!
""")

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

unicornhathd.brightness(1)

# We rotate the heart to be the same orientation as the text on the rear
# of the Unicorn Hat HD
unicornhathd.rotation(270)


heart = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

heart = numpy.array(heart)

# Define the brightness levels for the heartbeat (lower numbers are dimmer)
# We let the minimum brightness be 1 so that there is still a visible heart
rising = range(1, 10, 1)    # [1...9]
ba = range(10, 5, -1)       # [10...6]
dum = range(5, 10, 1)       # [5...9]
falling = range(10, 0, -1)  # [10...1]

# Join the ranges together
pattern = (rising, ba, dum, falling)
brightness_levels = list(itertools.chain.from_iterable(pattern))

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

    step = 0
    try:
        while True:
            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Checking if we are in an event...')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                                maxResults=5, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('You are free!')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                print(now)
                
                
            # Go through each brightness level in the pattern
            for level in brightness_levels:
                for x in range(16):
                    for y in range(16):
                        h = 0.0  # red
                        s = 1.0  # saturation at the top of the red scale
                        v = heart[x, y] * float(level) / 10     # brightness depends on range
                        r, g, b = colorsys.hsv_to_rgb(h, s, v)  # convert hsv back to RGB
                        red = int(r * 255.0)                    # makes 0-1 range > 0-255 range
                        green = int(g * 255.0)
                        blue = int(b * 255.0)
                        unicornhathd.set_pixel(x, y, red, green, blue)  # sets pixels on the hat
                unicornhathd.show()                             # show the pixels
                time.sleep(0.005)                               # tiny gap, sets frames to a smooth 200/sec
            time.sleep(0.8)                                     # waiting time between heartbeats

    except KeyboardInterrupt:
        unicornhathd.off()
        print("Press Ctrl-C to terminate while statement")
        pass


if __name__ == '__main__':
    main()
