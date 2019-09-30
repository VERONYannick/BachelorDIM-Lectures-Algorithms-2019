#import urlparse
import os
import pika
import env

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

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
                        body='verony!')
                        
print(" [x] Sent 'verony'")

connection.close()


