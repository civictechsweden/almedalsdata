import json
import scrapers.almedalsveckan_info as ai
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

for year in ai.AVAILABLE_YEARS:
    events = []

    # Download from source
    for type in ai.AVAILABLE_TYPES:
       type_events = ai.get_detailed_list(year, type)
       filename = '{} - {}'.format(year, type)

       Writer.write_csv(type_events, filename + '.csv')
       Writer.write_json(type_events, filename + '.json')

       events.extend(type_events)

    Writer.write_csv(events, f'{year} - events.csv')
    Writer.write_json(events, f'{year} - events.json')

    # Load from file
    # with open(f'{year} - events.json') as file_json:
    #     events = json.load(file_json)

    all_events.extend([reduce_event(event) for event in events])

if all_events:
    Writer.write_csv(all_events, 'summary.csv')
    Writer.write_json(all_events, 'summary.json')
