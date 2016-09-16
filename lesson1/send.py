#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# Подключение к брокеру на локальном хосте
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

# Создание очереди с именем hello, если ее не было
channel.queue_declare(queue='test_message')

# Отправка сообщение с точкой обмена (для определения куда отправлять) (exchange) по умолчанию,
# в очередь с именем hello (routing_key)
# и с сообщением "Hello World!'
channel.basic_publish(exchange='',
                      routing_key='test_message',
                      body='Hello 1c!')
print " [x] Sent 'Hello World!'"

connection.close()

# Для просмотра существующи очередей используется команда
# $ sudo rabbitmqctl list_queues