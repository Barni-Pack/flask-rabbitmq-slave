import pika
import os

# read rabbitmq connection url from enviroment variable
# ampq_url = os.environ['AMQP_URL']
# url_params = pika.URLParameters(ampq_url)
url_params = None


def produce_messages(
    message_body,
    message_amount,
):
    # connect to rabbitmq
    connection = pika.BlockingConnection(url_params)
    chan = connection.channel()

    # declare a new queue
    # durable flag is set so that messages are retained
    # in the rabbitmq volume even between restarts
    chan.queue_declare(queue='hello', durable=True)

    # publish 100 messages to the queue
    for i in range(message_amount):
        chan.basic_publish(
            exchange='',
            routing_key='hello',
            body=f'{message_body} {i + 1}',
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f'Produced message {i + 1}')

    # close the channel and connection
    # to avoid program from entering with any lingering
    # message in the queue cache
    chan.close()
    connection.close()
