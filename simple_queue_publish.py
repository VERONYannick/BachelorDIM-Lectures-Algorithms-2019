#import urlparse
import os
import pika
import env

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def publish(msg):
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

    channel = connection.channel()
    channel.queue_declare(queue='presentation’')
    channel.basic_publish(exchange='',
                            routing_key='presentation’',
                            body=msg)
                            
    print(" [x] Sent '",msg,"'")
    connection.close()


