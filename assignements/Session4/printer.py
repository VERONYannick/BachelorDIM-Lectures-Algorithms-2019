from threading import Thread

class Printer(Thread):
    """Thread to print console message"""

    def __init__(self):
        """Init async printer"""
        Thread.__init__(self)
        self.running=True
        self.queue=[]
        print("Printer Init")

    def addToQueue(self,str):
        """Function that put string into queue to be print when possible
        Args:
            str: text to print
        """
        self.queue.append(str)

    def run(self):
        """Function that print print queue content"""
                
        while self.running:
            if len(self.queue):
                print(self.queue[0])
                self.queue.pop(0)
                
    def stop(self):
        self.running=False