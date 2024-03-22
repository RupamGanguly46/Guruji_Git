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

t1start = time.time()
t1.start()
time.sleep(2)
should_run = False
t1.join()
t1close = time.time()

should_run = True

t2start = time.time()
t2.start()
time.sleep(2)
should_run = False
t2.join()
t2close = time.time()

print("Finished")
print(f"Thread 1: {t1close - t1start}\nThread 2 {t2close - t2start}")
