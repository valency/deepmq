import os
from datetime import datetime
from threading import Thread
from time import time

import pika

from static import FEEDS
from static import log, HOST, QUEUE, DATA_PATH


def subscribe(f):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    # channel.exchange_declare(exchange=feed['exchange'])
    # channel.queue_declare(queue=QUEUE)
    channel.queue_bind(queue=QUEUE, exchange=f['exchange'], routing_key=f['routing_key'])
    channel.basic_consume(callback, queue=QUEUE, no_ack=True)
    log('Exchange "' + f['exchange'] + '" with routing_key "' + f['routing_key'] + '" is now up and waiting for messages.', 'blue')
    channel.start_consuming()


def callback(ch, method, properties, body):
    log('Exchange "' + method.exchange + '" with routing_key "' + method.routing_key + '" received ' + str(len(body)) + ' bytes.')
    if method.exchange == '':
        log('Exchange is not provided, data will be discarded.', 'red')
    else:
        path = DATA_PATH + datetime.now().strftime('%Y-%m-%d') + '/'
        if not os.path.exists(path):
            os.makedirs(path)
        fn = method.exchange + '.' + method.routing_key + '.' + str(time()) + '.json'
        with open(path + fn, 'wb') as f:
            f.write(body)
        log('Saved to "' + fn + '".')


if __name__ == "__main__":
    for feed in FEEDS:
        t = Thread(target=subscribe, args=[feed])
        t.start()
