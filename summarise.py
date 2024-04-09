import json
from services.writer import Writer

def reduce_event(event):
    event.pop('description')
    event.pop('more_info')
    event.pop('speakers')
    event.pop('contact_person_1')
    event.pop('contact_person_2')
    event.pop('websites')
    event.pop('facebook')
    event.pop('twitter')
    event.pop('hashtags')

    return event

all_events = []

years = [i for i in range(2009, 2024 + 1) if i != 2020]

for year in years:
    with open(f'{year} - events.json') as file_json:
        events = json.load(file_json)
        print(f'{year}: {len(events)} events.')

        all_events.extend([reduce_event(event) for event in events])

if all_events:
    Writer.write_csv(all_events, 'summary.csv')
    Writer.write_json(all_events, 'summary.json')
