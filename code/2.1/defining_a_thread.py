import threading

def function(i):
    print("function call by thread %i\n" %i)

threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start() # thread calling the function
    t.join() # telling the thread to wait until threads finished execution
