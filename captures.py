import datetime
from collections import namedtuple


def parse_date(state_string):
    return datetime.datetime.strptime(state_string, '%Y-%m-%d %H:%M')


def make_legend(capture):
    return '{} on {:%Y-%m-%d %H:%M}'.format(capture.description, capture.start_date)


Capture = namedtuple('Capture', ('filename', 'description', 'start_date'))

commutes = [
    Capture(
        filename='capture-0-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2019-12-16 07:00')
    ),
    Capture(
        filename='capture-1-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2019-12-17 07:00')
    ),
    Capture(
        filename='capture-2-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2019-12-18 07:00')
    ),
    Capture(
        filename='capture-5-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2020-01-13 07:00')
    ),
    Capture(
        filename='capture-6-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2020-01-14 07:00')
    ),
    Capture(
        filename='capture-7-a4.pcap',
        description='trip from Kaufering to Garching Forschungszentrum',
        start_date=parse_date('2020-01-20 07:00')
    )
]

u2_to_messestadt = Capture(
    filename='capture-3-a4.pcap',
    description='U2 trip from Feldmoching to Messestadt Ost',
    start_date=parse_date('2019-12-19 12:07')
)

u2_to_feldmoching = Capture(
    filename='capture-4-a4.pcap',
    description='U2 trip from Messestadt Ost to Feldmoching',
    start_date=parse_date('2019-12-19 13:05')
)

u6_roundtrip = Capture(
    filename='capture-2-a1.pcap',
    description='U6 round trip Garching Forschungszentrum/Klinikum Großhadern',
    start_date=parse_date('2019-12-19 12:00')
)

munich_to_dortmund = Capture(
    filename='capture-3-a1.pcap',
    description='train trip Munich Central Station to Dortmund Central Station',
    start_date=parse_date('2019-12-24 07:21')
)
