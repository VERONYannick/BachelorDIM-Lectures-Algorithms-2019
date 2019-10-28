#import urlparse
import os
import pika
import env
import reader
import printer
import scanner
import time

count=1
ccrcy=False

def callback(ch, method, properties, body):
    """callback executed when a message is receive"""
    if ccrcy:
        ch.basic_ack(delivery_tag = method.delivery_tag)

    global count
    print("message n°",count,' : ')
    print(" [x] Received %r" % body)
    count+=1


def read(concurrency,nb_readers=1,slowMode=False):
    """Function that read cloudamqp 'presentation' queue
    """
    amqp_url=env.amqp_key

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)

    global ccrcy
    ccrcy=concurrency

    if concurrency:#if on concurrency mode, create readers
        readers =[]
        pr = printer.Printer()
        pr.start()
        for i in range(nb_readers):
            r=reader.Reader(url,pr,'presentation’',concurrency,"reader "+str(i),(i==1 and slowMode)) #if slow mode is enable, slow reader 1
            readers.append(r)
            r.start()
        sc = scanner.Scanner(readers,pr)
        sc.start()
        
    else :
        params = pika.URLParameters(url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params) # Connect to CloudAMQP

        channel = connection.channel()
        auto_acknow=not concurrency
        channel.queue_declare(queue='presentation’')
        channel.basic_consume(queue='presentation’',
                                on_message_callback=callback,                          
                                auto_ack=auto_acknow)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

