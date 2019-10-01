from threading import Thread

class Printer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.running=True
        self.queue=[]
        print("Printer Init")

    def addToQueue(self,str):
        self.queue.append(str)

    def run(self):
        while self.running:
            if len(self.queue):
                print(self.queue[0])
                self.queue.pop(0)
    def stop(self):
        self.running=False