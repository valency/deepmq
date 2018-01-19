import pika

from static import log, FEEDS, HOST, QUEUE


def send(exchange, routing_key, body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE)
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
    log('Sent ' + str(len(body)) + ' bytes.')
    connection.close()


if __name__ == "__main__":
    for feed in FEEDS:
        send(feed['exchange'], feed['routing_key'], 'Hello World!')
