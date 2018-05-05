from oauth2client import file, client, tools
from googleapiclient import discovery
from httplib2 import Http
import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('credentials.json')

def renew_credentials():
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
    return creds

# 2018-05-05 12:10:24.035346
# 2018-07-01T10:00:00-00:00
def get_events(creds, search_term):

    minus_one_year = datetime.datetime.utcnow() - datetime.timedelta(days=365)
    time_min_value = minus_one_year.isoformat() + 'Z'
    plus_one_month = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    time_max_value = plus_one_month.isoformat() + 'Z'
    
    service = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

    events_result = service.events().list(calendarId='primary', timeMin=time_min_value,
                                      timeMax=time_max_value,
                                      maxResults=250, singleEvents=True,
                                      orderBy='startTime',q=search_term).execute()
    events = events_result.get('items', [])

    summaries = []
    if not events:
        print('No event found.')
    for event in events:
        summaries.append(event['summary'])

    return summaries