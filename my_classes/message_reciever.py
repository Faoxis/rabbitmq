#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pika

class MessageReciever():
    def __init__(self, host='localhost'):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = connection.channel()
        self.method = None

    def waiting_message(self, queue, method, exchange='1c.new_test.direct'):
        self.channel.exchange_declare(exchange=exchange, type='direct', durable=True)
        self.channel.queue_declare(queue=queue, durable=True)

        self.method = method

        self.channel.queue_bind(exchange=exchange, queue=queue)


        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self._callback, queue=queue)

        # Этот метод запускает бесконечное ожидание сообщения и вызывает callback функцию когда это необходимо
        self.channel.start_consuming()

    def _callback(self, ch, method, properties, body):
        print('I am here')
        ch.basic_ack(delivery_tag=method.delivery_tag)
        self.method(body)

if __name__ == '__main__':
    def super_method(message):
        print 'hello with message {}'.format(message)

    MessageReciever().waiting_message('new_test_queue', super_method)