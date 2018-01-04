import threading
from time import sleep

def function1():
    print(threading.currentThread().getName() + str(' starting ... \n'))
    sleep(2)
    print(threading.currentThread().getName() + str(' exiting ...\n'))
    return

def function2():
    print(threading.currentThread().getName() + str(' starting ... \n'))
    sleep(2)
    print(threading.currentThread().getName() + str(' exiting ...\n'))
    return

def function3():
    print(threading.currentThread().getName() + str(' starting ... \n'))
    sleep(2)
    print(threading.currentThread().getName() + str(' exiting ...\n'))
    return

if __name__ == "__main__":
    t1 = threading.Thread\
         (name='1st function', target=function1)
    t2 = threading.Thread\
         (name='2nd function', target=function2)
    t3 = threading.Thread\
         (name='3rd function',target=function3)

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
