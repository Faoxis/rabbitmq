#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# This says that the binding is direct
channel.exchange_declare(exchange='direct_logs', type='direct')

# Once we disconnect the consumer the queue should be deleted. There's an exclusive flag for that.
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue # name of the queue

# Creating paths of binding
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# Make bindings for our queue "queue_name"
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

# Set binding as method of routing key and transmitting body
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()