from threading import Thread

class Scanner(Thread):
    """Thread to read console message"""

    def __init__(self,threads,printer):
        """Init async scanner"""
        Thread.__init__(self)
        self.running=True
        self.threads = threads
        self.printer=printer
        print("Scanner Init")


    def run(self):
        """Function that read console msg"""
        while self.running:
            stop=input("Press 'k' to kill all threads\n")
            if stop=='k':
                for t in self.threads:#kill all others threads
                    self.kill(t)
                self.kill(self.printer)
                self.kill(self)#kill itself
        
    def stop(self):
        self.running=False
        print("All process killed.")
    
    def kill(self,thread):
        """Kill process
        Arg : thread Thread : a thread to kill
        """
        if self.printer.running:
            self.printer.addToQueue('killing : '+str(thread))
        else:
            print('killing :',thread)

        thread.stop()