import pika
import env
import printer
from threading import Thread

class Reader(Thread):
    queue=""
    count=0
    def __init__(self,url,printer,queue="presentation’",concurrency=False,name="reader"):
        Thread.__init__(self)
        self.printer=printer
        self.url=url
        self.queue = queue
        self.concurrency=concurrency
        self.name=name


    def run(self):
        """Function that read cloudamqp queue"""
        
        # Parse CLODUAMQP_URL (fallback to localhost)
        params = pika.URLParameters(self.url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params) # Connect to CloudAMQP

        self.channel = connection.channel()
        auto_acknow=not self.concurrency
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_consume(queue=self.queue,
                                on_message_callback=self.callback,                          
                                auto_ack=auto_acknow)

        #print(' [',self.name,'] Waiting for messages. To exit press CTRL+C')
        self.printer.addToQueue('['+self.name+'] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self,ch, method, properties, body):
        """callback executed when a message is receive"""
        if self.concurrency:
            ch.basic_ack(delivery_tag = method.delivery_tag)

        self.count+=1
        #print(" [",self.name,"] message n°",self.count,' : ')
        #print(" [",self.name,"] Received %r" % body)
        self.printer.addToQueue(" ["+self.name+"] Received message n°"+str(self.count)+' : '+str(body))
    
    def stop(self):
        self.channel.stop_consuming()
        