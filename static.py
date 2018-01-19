from datetime import datetime

from termcolor import colored

FEEDS = [{
    'exchange': 'odds',
    'routing_key': 'odds.change'
}, {
    'exchange': 'odds',
    'routing_key': 'lcoo.match'
}, {
    'exchange': 'integration',
    'routing_key': 'bet.status'
}, {
    'exchange': 'integration',
    'routing_key': 'bet.clear.2'
}, {
    'exchange': 'integration',
    'routing_key': 'meta.info'
}, {
    'exchange': 'integration',
    'routing_key': 'lcoo.outright'
}, {
    'exchange': 'livescore',
    'routing_key': 'match'
}, {
    'exchange': 'livescout',
    'routing_key': 'sport.server'
}, {
    'exchange': 'livescore',
    'routing_key': 'round'
}]

HOST = 'drquant.avatarsys.org'
QUEUE = 'msbet'
DATA_PATH = './data/'


def log(msg, color='green'):
    print(colored(datetime.now(), color), msg)
