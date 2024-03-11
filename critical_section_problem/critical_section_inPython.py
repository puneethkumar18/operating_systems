from threading import *

count = 0
lock = Lock()

def task():
    global count
    lock.acquire()
    for i in range (100000):
        count += 1

    lock.release()


if __name__ == '__main__':
    t1 = Thread(target=task)
    t2  =Thread(target= task)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count)