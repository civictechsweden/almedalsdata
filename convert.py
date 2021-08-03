import json

from services.writer import Writer

events = []
filenames = []

for i in reversed(range(13, 640)):
    filenames.append(str(i) + ' 000.json')

for filename in filenames:
    try:
        with open(filename) as file_json:
            events.extend(json.load(file_json))
    except OSError as e:
        print('File not found: {}'.format(filename))

for i in range(2009, 2022):
    print(i)
    if i != 2020:
        Writer.write_csv(
            [event for event in events if str(i) in event['start']],
            '{} - events.csv'.format(i))
        Writer.write_json(
            [event for event in events if str(i) in event['start']],
            '{} - events.json'.format(i))

events_light = []

for event in events:
    event_light = event
    event_light.pop('description')
    event_light.pop('more_info')
    event_light.pop('speakers')
    event_light.pop('contact_person_1')
    event_light.pop('contact_person_2')
    event_light.pop('websites')
    event_light.pop('facebook')
    event_light.pop('twitter')
    event_light.pop('hashtags')

    events_light.append(event_light)

Writer.write_csv(events_light, 'summary.csv')
Writer.write_json(events_light, 'summary.json')
