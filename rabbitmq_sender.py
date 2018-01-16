from datetime import datetime

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='drquant.avatarsys.org'))
channel = connection.channel()

channel.queue_declare(queue='msbet')

channel.basic_publish(exchange='', routing_key='msbet', body='Hello World!')
print('[', datetime.now(), ']', 'Sent "Hello World!"')
connection.close()
