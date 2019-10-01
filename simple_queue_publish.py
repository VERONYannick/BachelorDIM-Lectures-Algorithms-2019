#import urlparse
import os
import pika
import env

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def publish(msg,concurrency,nb_msg):
    """Function that publish 'verony' on cloudamqp 'presentation' queue
    Args:
        msg: message to publish
    """
    amqp_url=env.amqp_key

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    properties=pika.BasicProperties(content_type="text/plain",delivery_mode=1)

    if concurrency:
        properties.delivery_mode=2

    channel = connection.channel()
    channel.queue_declare(queue='presentation’')
    for i in range(nb_msg):
        channel.basic_publish(exchange='',
                                routing_key='presentation’',
                                body=msg,
                                properties=properties) 
        print(" [x] Sent '",msg,"' n°",i+1)
    connection.close()


