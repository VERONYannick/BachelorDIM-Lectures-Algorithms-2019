#import urlparse
import os
import pika
import env

count=1

def callback(ch, method, properties, body):
    """callback executed when a message is receive"""

    global count
    print("message n°",count,' : ')
    print(" [x] Received %r" % body)
    count+=1


def read():
    """Function that read cloudamqp 'presentation' queue
    """
    amqp_url=env.amqp_key

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    channel = connection.channel()
    channel.queue_declare(queue='presentation’')
    channel.basic_consume(queue='presentation’',
                            on_message_callback=callback,                          
                            auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

