import threading as thr
import time

should_run = True

def looper(txt):
    global should_run
    while should_run:
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
should_run = False

t1.join()
t2.join()

print("Finished")
