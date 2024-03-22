import threading as thr
import time

def looper(txt):
    while True:
        print(txt)

def thread1():
    looper("first")

def thread2():
    looper("second")

t1 = thr.Thread(target=thread1)
t2 = thr.Thread(target=thread2)

t1.start()
t2.start()

time.sleep(2)

t1.join()
t2.join()

print("Finished")
