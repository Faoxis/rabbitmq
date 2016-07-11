#!/usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Этот метод позволяет передавать сообщение только тем подписчикам, что освободились
channel.basic_qos(prefetch_count=1)

# Этот метод позволяет готоворит о том, что функция callback получает сообщение из очереди с именем task_queue
channel.basic_consume(callback, queue='task_queue')

# Этот метод запускает бесконечное ожидание сообщения и вызывает callback функцию когда это необходимо
channel.start_consuming()