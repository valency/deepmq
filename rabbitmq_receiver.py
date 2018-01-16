from datetime import datetime
from time import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='drquant.avatarsys.org'))
channel = connection.channel()

channel.queue_declare(queue='msbet')


def callback(ch, method, properties, body):
    print('[', datetime.now(), ']', 'Received', len(body), 'bytes.')
    fn = str(time()) + '.json'
    with open(fn, 'wb') as f:
        f.write(body)
    print('[', datetime.now(), ']', 'Saved to "', fn, '".')


channel.basic_consume(callback, queue='msbet', no_ack=True)

print('[', datetime.now(), ']', 'Waiting for messages. To exit press CTRL+C.')
channel.start_consuming()
