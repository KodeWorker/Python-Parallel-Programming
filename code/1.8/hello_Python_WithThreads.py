from threading import Thread

from time import sleep

class TestThread(Thread):
    def __init__(self):
        super().__init__()
        self.message = 'Hello Parallel Python Thread!!\n'

    def print_message(self):
        print(self.message)

    def run(self):
        print('Thread Starting\n')
        x = 0
        while(x < 5):
            self.print_message()
            sleep(2)
            x += 1
        print('Thread Ended')

print('Process Started')

hello_Python = TestThread()
hello_Python.start()

print('Process Ended')
