#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys

# connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
# get channel - object
channel = connection.channel()

# Проверка очереди на ее наличие, durable делает очередь устойчивой
# Так мы можем быть уверены, что очередь task_queue не будет потеряна при перезапуске сервера RabbitMQ.
channel.queue_declare(queue='task_queue', durable=True)

# getting a new message
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Так мы можем быть уверены, что очередь task_queue не будет потеряна при перезапуске сервера RabbitMQ.
# Теперь необходимо пометить сообщения как устойчивые.
# Для этого нужно передать свойство delivery_mode со значением 2:
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print " [x] Sent %r" % (message,)
connection.close()
