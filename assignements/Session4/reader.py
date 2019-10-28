import pika
import env
import printer
import time
from threading import Thread

class Reader(Thread):
    """A process that read and print message from CloudAMQP"""
    queue=""
    count=0
    def __init__(self,url,printer,queue="presentation’",concurrency=False,name="reader",slowMode=False):
        Thread.__init__(self)
        self.printer=printer
        self.url=url
        self.queue = queue
        self.concurrency=concurrency
        self.name=name
        self.slowMode=slowMode


    def run(self):
        """Function that read cloudamqp queue"""
        
        # Parse CLODUAMQP_URL (fallback to localhost)
        params = pika.URLParameters(self.url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params) # Connect to CloudAMQP

        self.channel = connection.channel()
        auto_acknow=not self.concurrency
        self.channel.queue_declare(queue=self.queue,durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue,
                                on_message_callback=self.callback,                          
                                auto_ack=auto_acknow)
        initMsg = '['+self.name+'] Waiting for messages. To exit press CTRL+C'
        if self.slowMode:
            initMsg+=' (Slow mode)'
        self.printer.addToQueue(initMsg)
        self.channel.start_consuming()

    def callback(self,ch, method, properties, body):
        """callback executed when a message is received"""
        if self.slowMode:
            time.sleep(1)
        self.count+=1
        self.printer.addToQueue("["+self.name+"] Received message n°"+str(self.count)+' : '+str(body))
        if self.concurrency:
            ch.basic_ack(delivery_tag = method.delivery_tag)
    
    def stop(self):
        """stop channel consuming"""
        self.channel.stop_consuming()
        