import threading
from matrixled import MatrixLed

class LedRunner:
    def __init__(self):
        self.thread = None
        self.running = False

    def __repeat(self, func, args):
        while self.running:
            func(**args)

    def start(self, func, **kwargs):
        if self.thread is not None and self.thread.isAlive():
            self.stop()
        self.running = True
        self.thread = threading.Thread(target=self.__repeat, args=(func, kwargs))
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def once(self, func, **kwargs):
        if self.thread is not None and self.thread.isAlive():
            self.stop()
        func(**kwargs)
