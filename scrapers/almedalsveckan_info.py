import html
import re
import time

from datetime import date, datetime
from time import mktime
from bs4 import BeautifulSoup

from services.downloader import Downloader

AVAILABLE_YEARS = [2018, 2019, 2021]
AVAILABLE_TYPES = ['meeting']

PROGRAM_URL = 'https://program.almedalsveckan.info/event/search/events/{}/{}/{}'
EVENT_URL = 'https://program.almedalsveckan.info/event/user-view/{}'


def get_list(year, type):
    print('Getting results for page 1...')
    contents = Downloader.get_json(PROGRAM_URL.format(year, type, 0))
    totalCount = int(contents['totalCount'])
    number_of_pages = totalCount // 100 + 1

    results = get_ids(contents)

    for page in range(1, number_of_pages):
        print('Getting results for page {}...'.format(page + 1))
        results.extend(
            get_ids(Downloader.get_json(PROGRAM_URL.format(year, type, page))))

    return results


def get_info(id):
    contents = Downloader.get(EVENT_URL.format(id))

    htmlData = html.unescape(contents.decode('utf-8'))
    soup = BeautifulSoup(htmlData, 'html.parser')
    content = soup.select('div[class*=content_inner]')

    if len(content) < 2:
        return None
    else:
        content = content[1]

    dates = get_field(content, 'Dag')

    return {
        'title': content.find('h1').text,
        'organiser': get_field(content, 'Arrangör'),
        'start': str(dates['start']),
        'end': str(dates['end']),
        'category': get_field(content, 'Evenemangskategori'),
        'type': get_field(content, 'Evenemangstyp'),
        'topic_1': get_field(content, 'Ämnesområde'),
        'topic_2': get_field(content, 'Ämnesområde 2'),
        'language': get_field(content, 'Språk'),
        'place': get_field(content, 'Plats'),
        'description': get_field(content, 'Beskrivning av samhällsfrågan'),
        'more_info': get_field(content, 'Utökad information om evenemanget'),
        'speakers': get_field(content, 'Medverkande'),
        'contact_person_1': get_field(content, 'Kontaktperson 1'),
        'contact_person_2': get_field(content, 'Kontaktperson 2'),
        'websites': get_field(content, 'Webb'),
        'facebook': get_field(content, 'Facebook'),
        'twitter': get_field(content, 'Twitter'),
        'food': get_field(content, 'Förtäring'),
        'hashtags': get_field(content, '#hashtagg'),
        'page_views': int(get_field(content, 'Sidvisningar')),
        'id': id,
    }


def get_detailed_list(year, type):
    list = get_list(year, type)

    events = []

    for event in list:
        print('Getting info for event {} : {}...'.format(
            event['id'], event['title']))
        events.append(get_info(event['id']))

    return events


def get_ids(contents):
    results = []

    for result in contents['result']:
        results.append(get_id(result))

    return results


def get_id(block):
    htmlData = html.unescape(block)
    soup = BeautifulSoup(htmlData, 'html.parser')
    h2 = soup.select_one('div[class*=event_headline]').find('h2')
    id = int(h2.find('a')['href'].replace('/event/user-view/', ''))

    return {'title': h2.text, 'id': id}


def get_dates(string):
    string = string.replace('9::30', '09:30')
    string = string.replace('.', ':')
    string = string.replace('17:65', '17:55')
    string = string.replace('1/7 2009 HH:MM - HH:MM', '1/7 2009 00:00 - 00:00')

    if string == '15:00 - 16:30':
        print('caught')
        string = '29/6 2019 15:00 - 16:30'

    times = re.findall('\d\d:\d\d', string)
    dates = string.split(', ')

    if len(times) < 1:
        times = ['00:00']
        date_1 = dates[0]
        date_2 = dates[0]
    else:
        date_1 = dates[0].replace(' {} - {}'.format(times[0], times[1]), '')
        date_2 = dates[-1].replace(' {} - {}'.format(times[-2], times[-1]), '')

    return {
        'start': date_from(date_1, times[0]),
        'end': date_from(date_2, times[-1])
    }


def date_from(date_string, time_string):
    struct = time.strptime('{} {}'.format(date_string, time_string),
                           "%d/%m %Y %H:%M")
    return datetime.fromtimestamp(mktime(struct))


def get_field(content, title):

    if title == 'Beskrivning av samhällsfrågan':
        return content.select('p')[0].text.strip()
    elif title == 'Utökad information om evenemanget':
        if len(content.select('p')) > 1:
            return content.select('p')[1].text.strip()
        else:
            return None

    titles = content.select('div[class=leftcol]')
    values = content.select('div[class=rightcol]')

    for i in range(0, len(titles)):
        if title in titles[i].text:
            if title == 'Dag':
                return get_dates(values[i].text.strip())
            elif title == 'Medverkande':
                return [li.text.strip() for li in values[i].select('li')][:-1]
            elif title == 'Webb':
                return [a['href'] for a in values[i].select('a')]
            elif title == 'Förtäring':
                return values[i].text.strip() == 'Ja'
            return values[i].text.strip()

    return None
