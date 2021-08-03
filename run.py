import scrapers.almedalsveckan_info as ai
from services.writer import Writer

#for year in ai.AVAILABLE_YEARS:
#    for type in ai.AVAILABLE_TYPES:
#        events = ai.get_detailed_list(year, type)
#        filename = '{} - {}'.format(year, type)
#
#        Writer.write_csv(events, filename + '.csv')
#        Writer.write_json(events, filename + '.json')

for thousand in reversed(range(0, 650)):
    events = []

    for id in reversed(range((thousand - 1) * 100, thousand * 100)):
        print('Getting info for event {}...'.format(id))
        event = ai.get_info(id)

        if event:
            print('{} – {}'.format(event['title'], event['start']))
            events.append(event)

    if len(events) > 0:
        Writer.write_csv(events, str(thousand) + '00.csv')
        Writer.write_json(events, str(thousand) + '00.json')
