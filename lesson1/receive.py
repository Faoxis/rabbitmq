# -*- coding: utf-8 -*-
import pika

# Функция, которая бдет вызвана после получения сообщения из очереди
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)



# Подключение к брокеру на локальном хосте
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()



# Проверка очереди на наличие
channel.queue_declare(queue='hello')


# Данный метод говорит о том, что при принятии сообщения из очереди с именем hello будет вызвана функция callback
# no_ack=True - отключение подтверждения обработанного сообщения, по умолчанию no_ack=False
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


# Запуск бесконечного ожидания сообщений из очереди
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()


# Для просмотра существующи очередей используется команда
# $ sudo rabbitmqctl list_queues