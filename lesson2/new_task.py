#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys

# connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
# get channel - object
channel = connection.channel()

# checking existing of queue
channel.queue_declare(queue='task_queue', durable=True)

# getting a new message
message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print " [x] Sent %r" % (message,)
connection.close()
