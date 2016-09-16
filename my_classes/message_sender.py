import pika


class MessageSender():
    def __init__(self, host='localhost'):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = connection.channel()

    def send_message(self, queue, message, exchange='1c.new_test.direct'):
        self.channel.queue_declare(queue=queue, durable=True)

        self.channel.exchange_declare(exchange=exchange, type='direct', durable=True)

        self.channel.basic_publish(exchange=exchange,
                                   routing_key=queue,
                                   body=message,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2,  # make message persistent
                                   ))

if __name__ == '__main__':
    MessageSender().send_message('new_test_queue', 'Hello there!')


