"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from oauth2client import file
# import datetime
from google_client import renew_credentials, get_events

def get_notes_from_calendar(creds):

    summaries = get_events(creds, 'https')
    summaries.extend(get_events(creds, 'http'))

    print('nombre d\'events ', len(summaries))

    if not summaries:
        print('No summary found.')
    #for summary in summaries:
    #    print(summary)

    summariesSet = set(summaries)
    print('nombre d\'events uniques ', len(summariesSet))
    return summariesSet

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    creds = renew_credentials()

get_notes_from_calendar(creds)