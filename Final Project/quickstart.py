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

import unicornhathd


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

unicornhathd.rotation(0)
unicornhathd.brightness(0.6)


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
                
                
            step += 1
            for x in range(0, 16):
                for y in range(0, 16):
                    dx = 7
                    dy = 7

                    dx = (math.sin(step / 20.0) * 15.0) + 7.0
                    dy = (math.cos(step / 15.0) * 15.0) + 7.0
                    sc = (math.cos(step / 10.0) * 10.0) + 16.0

                    h = math.sqrt(math.pow(x - dx, 2) + math.pow(y - dy, 2)) / sc

                    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)

                    r *= 255.0
                    g *= 255.0
                    b *= 255.0

                    unicornhathd.set_pixel(x, y, r, g, b)

            unicornhathd.show()
            time.sleep(1.0 / 60)
    except KeyboardInterrupt:
        unicornhathd.off()
        print("Press Ctrl-C to terminate while statement")
        pass


if __name__ == '__main__':
    main()
