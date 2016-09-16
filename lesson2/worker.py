#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
channel.exchange_declare(exchange='1c.test.direct', type='direct')

channel.queue_bind(exchange='1c.test.direct', queue='task_queue')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(body.count('.'))
    print " [x] Done"
    # Это строка отправляет неподтвержденное сообщение в случае обрыва соединения
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Благодаря этому методу подписчик не получит новое сообщение, до тех пор пока не обработает и не подтвердит предыдущее.
# RabbitMQ передаст сообщение первому освободившемуся подписчику
channel.basic_qos(prefetch_count=1)

# Этот метод готоворит о том, что функция callback получает сообщение из очереди с именем task_queue
channel.basic_consume(callback, queue='task_queue')

# Этот метод запускает бесконечное ожидание сообщения и вызывает callback функцию когда это необходимо
channel.start_consuming()
