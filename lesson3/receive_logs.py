#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

# С помощью этого метода rabbitmq самостоятельно создает очередь с произвольным именем
# Secondly, once we disconnect the consumer the queue should be deleted. There's an exclusive flag for that.
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue # Получение имени очереди


# From now on the logs exchange will append messages to our queue.
channel.queue_bind(exchange='logs', queue=queue_name)


print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
